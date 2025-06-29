import functools

def frst_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        q = func(*args, **kwargs)
        print("end")
        return q
    return wrapper

@frst_decorator
def addition(i):
    return i + i


def repeat(num_times):
    def repeat_dec(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            for x in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return repeat_dec


@repeat(num_times = 3)
def greet(name):
    print(f'Hello {name}')


def debug(func):
    functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}"for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')
        result = func(*args, **kwargs)
        print(f'{func.__name__!r} printed {result} ')
        return result
    return wrapper


@debug
@frst_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi")

# say_hi()
# say_hi()
# say_hi()

## ----------------------------------------------------


import time
from functools import wraps

def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} ran in {end - start:.4f} seconds.')
        return result
    return wrapper

@log_time
def slow_function():
    time.sleep(2)
    print("Done!")

# slow_function()

# ---------------------------------------------------


def log_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[TIME INFO] {func.__name__} took {end - start:.4f} seconds to run")
        return res
    return wrapper

def validate_inputs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in list(args) + list(kwargs.values()):
            if not isinstance(arg, (int, float)):
                raise TypeError("Please only use numerical inputs")
        res = func(*args, **kwargs)
        print(f"[INPUT INFO] {func.__name__} returned {res}.")
        return res
    return wrapper


@log_timer
@validate_inputs
def add(a, b):
    return a + b

@log_timer
@validate_inputs
def subtract(a, b):
    return a - b

@log_timer
def sleep_task(seconds):
    time.sleep(seconds)
    print("Done!")

# add(10, 15)
# subtract(15, 20)
# sleep_task(3)
