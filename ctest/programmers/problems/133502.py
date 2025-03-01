# https://school.programmers.co.kr/learn/courses/30/lessons/133502 - 햄버거 만들기
# 1->2->3->1


def solution(ingredient):
    stack = []
    cnt = 0

    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for _ in range(4):
                stack.pop()

    return cnt
