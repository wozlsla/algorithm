# Fibonacci numbers


# Recursive (중복되는 연산이 많다)
def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


# Dynamic Programming
memo = {1: 1, 2: 1}


def fibo_dp(n):

    if n in memo:
        return memo[n]

    memo[n] = fibo_dp(n - 1) + fibo_dp(n - 2)

    return memo[n]
