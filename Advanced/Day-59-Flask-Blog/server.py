from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/55a84acc1ba7541787d6").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    # response = requests.get('https://api.npoint.io/bc626e1a1760737d55c2')
    # all_posts = response.json()
    return render_template("index.html", post_objects=post_objects)

@app.route('/contact')
def contact():
    # response = requests.get('https://api.npoint.io/bc626e1a1760737d55c2')
    # all_posts = response.json()
    return render_template("contact.html")

@app.route('/about')
def about():
    # response = requests.get('https://api.npoint.io/bc626e1a1760737d55c2')
    # all_posts = response.json()
    return render_template("about.html")

@app.route('/post')
def post():
    # response = requests.get('https://api.npoint.io/bc626e1a1760737d55c2')
    # all_posts = response.json()
    return render_template("post.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
