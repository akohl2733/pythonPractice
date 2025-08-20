def demo(*args, **kwargs):
    return args, kwargs

print(demo(1, 2, a=10, b=20))

# unpacking

def add(a, b): return a + b
pair = (3, 4)
print(add(*pair))

conf = {"a": 10, "b": 20}
print(add(**conf))

def make_multiplier(k):
    def multiply(x):
        return k * x
    return multiply

times3 = make_multiplier(3)
print(times3)
print(times3(10))