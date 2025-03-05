# https://school.programmers.co.kr/learn/courses/30/lessons/12906 - 같은 숫자는 싫어
from collections import deque


def solution(arr):
    arr = deque(arr)

    result = [arr.popleft()]

    while arr:
        i = arr.popleft()
        if result[-1] != i:
            result.append(i)

    return result


"""
연속된 중복을 제거하는 방법 (성능은 O(n)으로 동일)
itertools.groupby : 내부적으로 연속된 동일 요소들을 그룹화하여 처리
- 시퀀스에서 연속적으로 같은 값이 나타나는 구간을 하나의 그룹으로 묶음
- 각 그룹은 (key, group_iterator) 형태의 튜플로 반환
print : 4,4,4 -> 3,3 -> 4
"""
from itertools import groupby


def solution(arr):
    return [key for key, _ in groupby(arr)]


def solution(arr):
    li = []
    for key, group in groupby(arr):
        group_list = list(group)  # iterator
        print(f"키: {key}, 그룹: {group_list}")
        li.append(key)

    return li


# print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3, 4]))


""" 성능 확인 
groupby_solution: 1.983315749996109
manual_solution: 2.3064023749975604

파이썬 코드 레벨에서 직접 구현한 반복문보다 내부적으로 C로 최적화되어 실행.

즉, groupby는 C 코드로 구현되어 있어서, 그룹핑 작업 자체가 매우 빠르게 수행됨. 리스트 컴프리헨션 역시 파이썬 바이트코드로 최적화되어 있어, 일반적인 파이썬 for 루프보다 효율적.
"""
import timeit, itertools


def groupby_solution(arr):
    return [k for k, _ in itertools.groupby(arr)]


def manual_solution(arr):
    if not arr:
        return []
    result = [arr[0]]
    for i in arr[1:]:
        if i != result[-1]:
            result.append(i)
    return result


# 테스트를 위한 예시 데이터 (연속된 중복이 많은 경우)
arr = [1, 1, 2, 2, 2, 3, 3] * 10000

print("groupby_solution:", timeit.timeit(lambda: groupby_solution(arr), number=1000))
print("manual_solution:", timeit.timeit(lambda: manual_solution(arr), number=1000))
