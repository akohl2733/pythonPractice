example = [x ** 2 for x in range(10)]
# print("Base example:", example)

example2 =  [x ** 2 for x in range(10) if x % 2 == 0]
# print("Example with conditional:", example2)

nums = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']     # Does not have to be the same index to work - one can be larger than the other
example3 = [[n, l] for n in nums for l in letters]
# print("Example with 2 lists:", example3)

itr_string = "some text"
example4 = [l for l in itr_string if l!=" "]
# print("Example for list without spaces:", example4)

dict_comp = {x:chr(65+x-1) for x in range(1, 11)}
# print(type(dict_comp))
# print("Example with dictionary comprehension", dict_comp)

set_comp = {x ** 3 for x in range(1, 6)}
# print(type(set_comp))
# print(set_comp)

customers = [{"is_dm2_passed": False}, {"is_dm2_passed": True}]
print(all(customer["is_dm2_passed"] for customer in customers))