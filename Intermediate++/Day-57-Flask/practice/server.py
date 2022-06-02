from flask import Flask, render_template
import requests
import datetime
app = Flask(__name__)


@app.route('/')
def home():
    my_name = "paulipotter"
    current_year = datetime.datetime.today().year
    return render_template('index.html', current_year=current_year, my_name=my_name)


@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    response = requests.get(gender_url)
    response.raise_for_status()
    gender = response.json()['gender']
    age_url = f"https://api.agify.io?name={name}"
    response2 = requests.get(age_url)
    age = response2.json()['age']

    return render_template('name.html', name=name, age=age, gender=gender)


@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/bc626e1a1760737d55c2"
    response = requests.get(blog_url)
    response.raise_for_status()
    blogs = response.json()
    return render_template('blog.html', posts=blogs)

if __name__ == "__main__":
    app.run(debug=True)


