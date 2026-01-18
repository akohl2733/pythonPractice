def fib(n, d={}):
    if n in d:
        return d[n]
    if n <= 1:
        return n
    else:
        res = fib(n-1, d) + fib(n-2, d)
        d[n] = res
    return res


def detect_dupes(l):
    seen = set()
    res = []

    for e in l:
        if e in seen:
            res.append(e)
        else:
            seen.add(e)

    return res


def factorial(i):
    if i == 0 or i == 1:
        return i
    elif i > 1:
        return i * factorial(i-1)
    

def sum_of_digits(i):
    pass