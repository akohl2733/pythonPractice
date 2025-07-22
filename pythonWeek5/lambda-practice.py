from typing import Callable


x: Callable[[list[int]], float] = lambda y: sum([q * 5 for q in y]) / len(y)

nums = [1, 2, 3, 4, 5]
print(x(nums))