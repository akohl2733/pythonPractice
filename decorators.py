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

say_hi()
say_hi()
say_hi()

