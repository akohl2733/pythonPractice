def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)


doubles = [2 * n for n in range(50)]
gen_doubles = list(2 * n for n in range(50))

print(doubles, gen_doubles)