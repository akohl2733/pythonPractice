square = lambda x: x*x
# print(square(10))

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x*x, nums))
# print(squared)

filtered = list(filter(lambda x: x % 2 == 0, nums))
# print(filtered)

from functools import reduce
reduced = reduce(lambda acc, x: x + acc, nums, 0)
# print(reduced)

# ---------------------------------

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 24},
    {"name": "Charlie", "age": 35},
    {"name": "Diana", "age": 28}
]

older_than = list(filter(lambda x: x["age"] > 28, people))
# print(older_than)
old_map = list(map(lambda x: x["name"], older_than))
# print(old_map)
total_age = reduce(lambda acc, x: acc + x['age'], people, 0)
# print(total_age)

# ------------------------------------

avg_age = reduce(lambda arr, x: arr + x['age'], people, 0) / len(people)
# print(avg_age)

highest_age = reduce(lambda a, b: a if a['age'] > b['age'] else b, people)
# print(highest_age)

youngins = list(map(lambda x: x['name'], list(filter(lambda x: x['age'] < 30, people))))
# print(youngins)

# ---------------------------------------------

prices = [10.99, 5.50, 3.75, 8.20]
res = list(map(lambda x: float(f"{x * 1.08:.2f}"), prices))
# print(res)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divideThree = list(filter(lambda x: x % 3 == 0, numbers))
# print(divideThree)
bums = [2, 3, 4, 5]
prod = reduce(lambda arr, x: arr * x, bums, 1)
# print(prod)

# -------------------------------------------

products = [
    {"name": "Keyboard", "price": 50},
    {"name": "Monitor", "price": 300},
    {"name": "Mouse", "price": 25}
]

final = list(map(lambda x: x['name'], list(filter(lambda x: x['price'] < 100, products))))
print(final)