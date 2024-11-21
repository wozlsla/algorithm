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


# 극장 좌석 자리 구하기
def cal_seat(n, vips):
    res = 1

    memo = {
        0: 1,
        1: 1,
        2: 2,
    }

    def dp(n):
        if n in memo:
            return memo[n]
        memo[n] = dp(n - 1) + dp(n - 2)
        return memo[n]

    # 1 2 {3} 4 5 {6} 7 8 9
    bf_vip = 0
    for vip in vips:
        cnt = dp(vip - 1 - bf_vip)
        res *= cnt
        bf_vip = vip

    res *= dp(n - bf_vip)
    return res
