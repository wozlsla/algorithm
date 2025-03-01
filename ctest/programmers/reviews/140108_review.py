# https://school.programmers.co.kr/learn/courses/30/lessons/140108 - 문자열 나누기

from collections import deque


def solution(s):

    x = not_x = cnt = 0
    s = deque(s)

    while s:  # empty deque == false

        char = s.popleft()
        x += 1

        for _ in range(len(s)):
            if char == s.popleft():
                x += 1
            else:
                not_x += 1

            if x == not_x:
                cnt += 1
                x = not_x = 0
                break

    return (cnt + 1) if x > 0 else cnt


def solution(s):
    x = not_x = cnt = 0

    for i in s:
        if x == not_x:
            cnt += 1
            char = i  # 기준 문자 설정 (update)

        if i == char:
            x += 1
        else:
            not_x += 1

    return cnt


# queue 중첩 반복문 제거
def solution(s):
    s = deque(s)
    x = not_x = cnt = 0
    current_char = None

    while s:
        char = s.popleft()

        if x == not_x:
            cnt += 1
            current_char = char
            x = not_x = 0

        if char == current_char:
            x += 1
        else:
            not_x += 1

    return cnt


print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
