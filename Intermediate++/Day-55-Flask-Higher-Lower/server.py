from random import randint
from flask import Flask
import time

app = Flask(__name__)
random_number = randint(0,10)


@app.route('/')
def homepage():
    return 'homepage'


@app.route('/<num>')
def guess_number(num):
    num = int(num)
    if random_number > num:
        return 'too small'
    elif random_number < num:
        return 'too big'
    else:
        return 'you got it!'


if __name__ == '__main__':
    app.run(debug=True)