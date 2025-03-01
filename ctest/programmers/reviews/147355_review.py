# https://school.programmers.co.kr/learn/courses/30/lessons/147355 - 크기가 작은 부분 문자열


def solution(t, p):

    cnt = 0
    window = len(p)
    p = int(p)

    # 움직인다의 표현..? slicing

    for i in range(len(t) - window + 1):
        # print(int(t[i : i + window]))
        if int(t[i : i + window]) <= p:
            cnt += 1

    return cnt


# print(solution("3141592", "271"))
# print(solution("500220839878", "7"))
solution("500220839878", "72")
"""
python 정수 처리 방식 : 선행 0은 무시됨
50
0
2
22
20
8
"""


def solution(t, p):
    return len(
        [
            t[i : i + len(p)]
            for i in range(len(t) - len(p) + 1)
            if int(t[i : i + len(p)]) <= int(p)
        ]
    )
