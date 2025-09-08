from functools import wraps

def task(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    wrapper.is_task = True
    return wrapper

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, fn):
        if not getattr(fn, "is_task", False):
            raise ValueError("Only decorated functions can be added")
        self.tasks.append(fn)

    def run(self):
        for fn in self.tasks:
            yield fn()

scheduler = TaskScheduler()

@task
def say_hello():
    return "Hello!"

@task
def add_numbers():
    return 2 + 3

scheduler.add_task(say_hello)
scheduler.add_task(add_numbers)
for result in scheduler.run():
    print(result)