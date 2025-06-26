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
    
for num in MyRange(1, 5, 0):
    print(num)