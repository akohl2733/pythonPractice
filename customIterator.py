class MyRange:

    def __init__(self, start, stop, step=1):
        if step == 0:
            raise ValueError("Step cannot be zero.")
        self.curr = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.step > 0:
            if self.curr >= self.stop:
                raise StopIteration
        else:
            if self.curr <= self.stop:
                raise StopIteration
        value = self.curr
        self.curr += self.step
        return value       
    
total = sum(num for num in MyRange(10, 31) if num % 2 == 0)

# print(total)

# -------------------------------------------
# Generator

def fibonacci(n):
    x, y = 0, 1
    for _ in range(n):
        yield x
        x, y = y, x+y

# for n in fibonacci(7):
#     print(n)

# ----------------------

def evensToNumber(num):
    for i in range(num + 1):
        if i%2 == 0: yield i


nums = list(evensToNumber(56))
print(nums)

# -----------------------------

def square_up_to(num):
    for i in range(num + 1):
        yield i * i