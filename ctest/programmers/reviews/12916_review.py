# https://school.programmers.co.kr/learn/courses/30/lessons/12916 - 문자열 내 p와 y의 개수


def solution(s):
    p = y = 0

    p = s.lower().count("p")
    y = s.lower().count("y")

    if p == 0 and y == 0:
        return True

    return True if p == y else False


"""
조건 검사 중복 됨.
같지 않을경우 False 를 제외하고 모두 True.
조건 분리가 명확히 돼야 함.
"""


from collections import Counter


def solution(s):
    c = Counter(s.lower())
    return c["y"] == c["p"]
