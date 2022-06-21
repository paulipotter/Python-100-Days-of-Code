from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///my-top-movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(200), unique=False, nullable=False)
    img_url = db.Column(db.String(300), unique=False, nullable=False)

    def __repr__(self):
        return '<Author %r>' % self.author


class RateMovieForm(FlaskForm):
    rating = FloatField('Enter your Rating', validators=[DataRequired()])
    review = StringField('Enter your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddMovie(FlaskForm):
    movie_name = StringField("Enter the movie you'd like to add", validators=[DataRequired()])
    submit = SubmitField('Submit')


new_movie = Movies(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)
db.create_all()
# db.session.add(new_movie)
# db.session.commit()

@app.route("/")
def home():
    all_movies_db = db.session.query(Movies).all()
    return render_template("index.html", all_movies_db=all_movies_db)


@app.route("/add")
def add():
    form = AddMovie()
    if form.validate_on_submit():
        pass
    return render_template("add.html", form=form)


@app.route('/edit', methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    if form.validate_on_submit():
        movie_id = request.args.get('id')
        update_movie = Movies.query.get(movie_id)
        update_movie.rating = form.rating.data
        update_movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    # Retrieve movie and render edit.html
    movie_id = request.args.get('id')
    movie_to_update = Movies.query.get(movie_id)
    return render_template("edit.html", movie=movie_to_update, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movies.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
