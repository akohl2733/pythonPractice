def countdown(num):
    while num >= 0:
        yield num
        num -= 1

# ctr = countdown(10)
# for c in ctr:
#     print(c)

class EvenNumbers:

    def __init__(self, limit: int):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 2
        return value