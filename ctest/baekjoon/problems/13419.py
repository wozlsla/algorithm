# https://www.acmicpc.net/problem/13419 - 탕수육

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    first = []
    second = []
    s = input().strip()

    if len(s) == 1:
        print(s, s, sep="\n")
        continue

    c = 0
    stop = True
    while stop:
        for i in range(1, len(s) + 1):
            if (i + c) % 2 == 0:
                second.append(s[i - 1])
            else:
                first.append(s[i - 1])
                if first.count(s[0]) == 2:
                    first.pop()
                    stop = False
                    break

        c += 1

    print("".join(first))
    print("".join(second))
# ABCDE
# ACEBD A
# BDACE B

# ABCDEFG
# ACEGBDF A
# BDFACEG B

# ABCDEFGH
# ACEG A
# BDFH B


# 다른 사람 풀이
t = int(input())
games = []

for _ in range(t):
    games.append(input())

for game in games:
    jjagsu_chars = ""
    holosu_chars = ""

    for i in range(len(game)):
        if i % 2 == 0:  # 짝수 인덱스일 때
            jjagsu_chars += game[i]
        else:
            holosu_chars += game[i]

    if len(game) % 2 == 0:  # 문자열 길이가 짝수일 때
        print(jjagsu_chars)
        print(holosu_chars)
    else:  # 문자열 길이가 홀수일 때
        print(jjagsu_chars + holosu_chars)
        print(holosu_chars + jjagsu_chars)

# 2
import sys

lines = sys.stdin.read().splitlines()
N = int(lines[0])

for line in lines[1:]:
    if len(line) % 2 == 1:
        line *= 2

    print(line[::2])
    print(line[1::2])
