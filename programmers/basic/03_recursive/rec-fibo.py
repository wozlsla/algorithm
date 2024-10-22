def solution(n):
    f0, f1 = 0, 1

    if n == 0:
        return f0

    elif n < 2:
        return f1

    return solution(n - 1) + solution(n - 2)


"""
1. 중복 계산 문제: 현재 이 코드는 재귀 호출로 fibonacci(n-1)과 fibonacci(n-2)를 호출하는데, 이 방식은 많은 중복 계산을 발생시킵니다. 예를 들어 fibonacci(5)를 계산하려면 fibonacci(4)와 fibonacci(3)을 계산하고, 또다시 fibonacci(4)에서 fibonacci(3)과 fibonacci(2)를 반복해서 계산하는 방식입니다. 이로 인해 시간 복잡도가 지수적으로 증가하므로 큰 n에 대해 매우 비효율적입니다. O(2^n)

2. 불필요한 변수 초기화: f0, f1 변수가 선언되었지만 이 변수는 재귀 호출에서 전혀 사용되지 않습니다. 따라서 불필요한 변수입니다. 
"""


def solution(n):
    if n <= 1:
        return n

    return solution(n - 1) + solution(n - 2)


""" 반복문을 사용하면 중복 계산을 줄이고 시간 복잡도를 크게 줄일 수 있습니다. O(n)"""


def solution(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    elif n <= 2:
        return 1

    for i in range(n - 1):  # 0, n-1
        k = a + b
        a = b
        b = k

    return k


def solution(n):
    if n <= 1:
        return n

    f0, f1 = 0, 1
    for _ in range(2, n + 1):
        f0 = f1
        f1 = f0 + f1

    return f1


print(solution(4))
