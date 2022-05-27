from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, world!'


if __name__ == '__main__':
    app.run()

import time


##  Python Decorator Function - function that wraps another one and gives additional functionality
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function()


@delay_decorator
def say_hello():
    print("hello!")

def say_greeting():
    print("greetings")


decorated_function = delay_decorator(say_greeting)
decorated_function()