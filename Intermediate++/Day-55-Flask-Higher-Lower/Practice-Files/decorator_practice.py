
#  here you have a regular old user class
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

#  decorator function
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs): # add args and kwargs to take care of any potential function arguments
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

#  decorator function checks if user is logged in
@is_authenticated_decorator
def create_blog_post(user):
    #  function runs only if logged in == true
    print(f"This is {user.name}'s new blog post.")

