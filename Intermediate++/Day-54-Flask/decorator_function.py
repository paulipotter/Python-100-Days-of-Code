import time
current_time = time.time()
print(current_time)



def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time() # get start time
        function() # run wrapped function
        end_time = time.time() # get end time
        print(f"{function.__name__} run speed: {end_time - start_time}s") # print how long it took the function to run
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

slow_function()
fast_function()