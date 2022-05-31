from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, world!'


def make_bold(function):
    def wrapper(*args, **kwargs):
        line = f"<b>{args[0]}</b>"
        function()
    return wrapper()


def say_greeting():
    print("greetings")


decorated_function = delay_decorator(say_greeting)
decorated_function()

if __name__ == '__main__':
    app.run(debug=True)

def make_bold(function):
    def wrapper(*args, **kwargs):
        line = f"<b>{args[0]}</b>"
        function(line)
    return wrapper