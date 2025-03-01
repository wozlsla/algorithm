# !! 구현보다, 문제에 어떻게 접근해야할지 먼저 생각하고 들어가기

from itertools import combinations


# 시간 초과
def solutions(nums):

    n = len(nums) // 2
    kind = 0

    for i in combinations(nums, n):
        if len(set(i)) >= kind:
            kind = len(set(i))

    return kind


"""
사용자의 코드가 비효율적인 이유는 모든 가능한 조합을 생성하고 이를 반복하여 검사하기 때문입니다. 

주어진 문제는 폰켓몬의 종류를 최대한 많이 포함하여 N/2 마리를 고르는 것입니다. 
이 경우, 실제로 모든 조합을 고려할 필요가 없습니다. 폰켓몬의 종류 수가 N/2 보다 많거나 같다면, 최대로 고를 수 있는 종류의 수는 N/2 입니다. 만약 종류의 수가 N/2 보다 적다면, 그 종류의 수만큼만 고를 수 있습니다.
"""


def solution(nums):
    n = len(nums) // 2
    unique = len(set(nums))

    if unique < n:
        return unique

    return n


# 다른 사람 풀이
def solution(nums):
    return min(len(nums) / 2, len(set(nums)))


nums = [3, 3, 3, 2, 2, 4]
nums = [3, 3, 3, 2, 2, 2]
print(solution(nums))
