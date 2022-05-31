# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"{function.__name__} was called!")
        function()
    return wrapper


# Use the decorator 👇
@logging_decorator
def hello_world():
    print("hello, world!")

hello_world()