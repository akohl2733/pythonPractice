names = ["Chloe", "Zeke", "Lu"]

nameiterator = iter(names)

# print(next(nameiterator))
# print(next(nameiterator))
# print(next(nameiterator))


class SkipRange:

    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.step > 0:
            if self.start >= self.stop:
                raise StopIteration
            val = self.start
            self.start += self.step
        else:
            if self.start < self.stop:
                raise StopIteration
            val = self.start
            self.start += self.step
        return val
    

for e in SkipRange(10, 2, -2):
    print(e)



# class getOBJ:

#     def __init__(self):
#         self.data = [1, 2, 3]
    
#     def __getitem__(self, index):
#         return self.data[index]
    
# for x in getOBJ():
#     print(x)


class EveryThird:

    def __init__(self, total):
        self.duck = "Duck"
        self.goose = "Goose"
        self.total = total
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count > self.total:
            raise StopIteration
        self.count += 1
        if (self.count) % 3 == 0:
            return self.goose + "\n"
        else:
            return self.duck
        
for i in EveryThird(20):
    print(i)