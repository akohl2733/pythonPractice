def fib(n):
    
    memo = [-1] * (n+1)

    if n <= 1:
        return n

    if memo[n] != -1:
        return memo[n]

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

print(fib(10))