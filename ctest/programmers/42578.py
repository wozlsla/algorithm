# https://school.programmers.co.kr/learn/courses/30/lessons/42578
import math

item = {}


def solution(clothes):
    """
    ! 각 종류별로 입을 수 있는 경우의 수는 (해당 의상 개수 + 1)
      여기서 +1은 `그 종류의 의상을 입지 않는 경우`를 포함

    math.prod(): 반복 가능한 객체의 모든 요소를 곱합 (>= Python 3.8)
    """

    for i in clothes:
        item[i[1]] = item.get(i[1], 0) + 1

    # 아무것도 입지 않는 경우를 제외 (-1)
    return math.prod([i + 1 for i in item.values()]) - 1


clothes = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
]

clothes = [
    ["crow_mask", "face"],
    ["blue_sunglasses", "face"],
    ["smoky_makeup", "face"],
]

print(solution(clothes))


# 다른 사람 풀이 (Counter, reduce)
from collections import Counter
from functools import reduce


def solution(clothes):
    cnt = Counter([ctype for _, ctype in clothes])  # <str, int>
    return reduce(lambda a, b: a + b + a * b, cnt.values())
    # return reduce(lambda a, b: a * (b + 1), cnt.values(), 1) - 1
