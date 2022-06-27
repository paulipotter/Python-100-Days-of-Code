from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

all_books = []


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Author %r>' % self.author


db.create_all()


@app.route('/')
def home():

    all_books_db = db.session.query(Books).all()
    return render_template('index.html', all_books_db=all_books_db)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_submission = Books(title=request.form['title'],
                                author=request.form['author'],
                                rating=request.form['rating'])

        db.session.add(book_submission)
        db.session.commit()

        # book_submission = {
        #     "title": request.form['title'],
        #     "author": request.form['author'],
        #     "rating": request.form['rating']
        # }
        #
        # all_books.append(book_submission)

        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #  use the ID gotten in the form to query the same book from the database
        update_book = Books.query.get(request.form['id'])
        update_book.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))

    # Get book id of book that will be deleted
    book_id = request.args.get('id')

    # Query book that was chosen to edit rating
    book_selected = Books.query.get(book_id)
    return render_template("edit.html", book=book_selected)


@app.route('/delete')
def delete():
    # Get book id that's passed in
    book_id = request.args.get('book_id')
    print("book id is", book_id)
    # Query book using ID
    book = Books.query.get(book_id)
    print("book is", book)

    # Delete the previously queried record
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
