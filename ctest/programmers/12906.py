result = []


def solutions(arr):
    n = None  # 초기값 고려 필

    for i in arr:
        if n == None or n != i:
            result.append(i)
            n = i
    return result


result = []
print(result[-1:])


def solutions(arr):

    for i in arr:
        if not result or result[-1] != i:
            result.append(i)

    return result


"""다른 사람 풀이
a[-1:]: 리스트 a의 마지막 요소를 `리스트 형태`로 가져옴 (slicing)
a가 비어 있을 때에도 오류 없이 `빈 리스트 []`를 반환
"""


def solution(s):
    a = []
    for i in s:
        if a[-1:] == [i]:
            continue
        a.append(i)
    return a


# arr = [1, 1, 3, 3, 0, 1, 1]
# arr = [4, 4, 4, 3, 3]
arr = [0, 4, 4, 4, 3, 3]
print(solution(arr))
