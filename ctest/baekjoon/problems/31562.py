# https://www.acmicpc.net/problem/31562 - 전주 듣고 노래 맞히기

import sys

data = sys.stdin.read().splitlines()

N, M = map(int, data[0].split())

dic = {}

for i in range(1, N + 1):
    line = data[i].split()
    dic[line[1]] = "".join(line[2:5])

lines = data[-M:]
codes = ["".join(line.split()) for line in lines]


for code in codes:
    cnt = sum(1 for v in dic.values() if v == code)

    if cnt > 1:
        print("?")
    elif cnt == 0:
        print("!")
    else:
        print(next(k for k, v in dic.items() if v == code))  # generator
        # print([k for k, v in dic.items() if v == code][0])


"""
key 는 중복이 안되기 때문에 value로 검사
-> 조건을 보면 중복이면 바로 "?" 를 print 하면 됨...

Search Key/Value -> Key로 변환
https://www.acmicpc.net/source/84418541
"""

for _ in range(1, N + 1):
    line = data[i].split()
    song = " ".join(line[2:5])

    if song in dic:
        dic[song] = "?"
    else:
        dic[song] = line[1]

for line in lines:
    if line in dic:
        print(dic[line])
    else:
        print("!")
