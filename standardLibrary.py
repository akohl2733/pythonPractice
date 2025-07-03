from collections import Counter

fruits = ['apple', 'banana', 'grapefruit', 'banana', 'apple', 'apple']
totals = Counter(fruits)

# print(totals)
# print("Most popular:", totals.most_common(1))


# ---------------------------------------------

from itertools import chain

a = [1, 2]
b = [3, 4]

# for x in chain(a, b):
#     print(x)


# -------------------------------------

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 0:
        raise ValueError("Input must not be negative")
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# print(fib(35))

# -------------------------------------
import re

text = "apple banan-+a app?le orANge banana apple ki!!wi ki.wi banana"
cleaned_text = re.sub(r'[\.\?\!,-_=+]', "", text).lower()

text_list = cleaned_text.split()
total = Counter(text_list)

print(total.most_common(3))