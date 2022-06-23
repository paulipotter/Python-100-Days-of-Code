from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import os
import requests

app = Flask(__name__)
# SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Create DB
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///my-top-movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)

TMDB_KEY = os.environ.get('TMDB_KEY')
TMDB_URL = 'https://api.themoviedb.org/3/search/movie'
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


# Create table
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(200), unique=False, nullable=True)
    img_url = db.Column(db.String(300), unique=False, nullable=False)



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
    all_movies = Movies.query.order_by(Movies.rating).all()
    print(all_movies)
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", all_movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        parameters = {
            'api_key': TMDB_KEY,
            'query': form.movie_name.data
        }
        response = requests.get(TMDB_URL, params=parameters)
        response.raise_for_status()
        data = response.json()['results']
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route('/edit', methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movies.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movies.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/find')
def find():
    movie_api_id = request.args.get('id')
    MOVIE_DB_INFO_URL = f'https://api.themoviedb.org/3/movie/'

    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": TMDB_KEY, "language": "en-US"})
        data = response.json()
        print("DATA", data)
        new_movie = Movies(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
    return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
