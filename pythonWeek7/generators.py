# print(hasattr(list, '__iter__'))

simple_list = [1, 2, 3]
my_itr = iter(simple_list)
# print(my_itr)

# print(next(my_itr))
# print(next(my_itr))
# print(next(my_itr))
# print(next(my_itr))   ->  This leads to StopIteration as it is past the range of simple_list

list_comp = [x ** 2 for x in range(10) if x % 2 == 0]
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)

# print(list_comp)    ->  [0, 4, 16, 36, 64]
# print(gen_exp)  ->  <generator object <genexpr> at 0x7fa7cb6df9f0>

from sys import getsizeof

my_comp = [x * 5 for x in range(1000)]
my_gen = (x * 5 for x in range(1000))

# print(getsizeof(my_comp)) ->  8856
# print(getsizeof(my_gen))  ->  200  ->  takes much less memory but slower

def squares(length):
    for n in range(length):
        yield n ** 2

# for square in squares(5):
#     print(square)

cubes = (x ** 3 for x in range(5))
for cube in cubes:
    print(cube)


# a list comprehension creates all elements right away and loads all of them into the memory
# a generator expression creates a single element based on request. It loads only one single element to the memory

sqs = (i*i for i in range(10000000))
first_div_97 = next(x for x in sqs if x % 97 == 0)  # ->    this would be best for generators because you don't need all values

vals = [f(x) for x in range(100000)]
do_something(vals)
do_something_else(vals) # ->    reuse - generators would be exhausted - go with lists