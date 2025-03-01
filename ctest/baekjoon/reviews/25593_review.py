# https://www.acmicpc.net/problem/25593 - 근무 지옥에 빠진 푸앙이 (Small)

import sys

# data = lambda: sys.stdin.readline().strip("\n")

# 전체 입력을 한 번에 읽어서 리스트로 저장 (I/O 횟수를 줄임)
data = sys.stdin.read().splitlines()

weeks = int(data[0])
time = [4, 6, 4, 10]
table = {}

idx = 1

for _ in range(weeks):
    for i in time:
        for name in data[idx].split():
            if name != "-":
                table[name] = table.get(name, 0) + i
        idx += 1

if not table:
    print("Yes")
elif max(table.values()) - min(table.values()) <= 12:
    print("Yes")
else:
    print("No")


""" 
각 인원의 근무 시간이 12시간 이하로 차이 나게 해서 최대 50주 치 근무표
근무 타임 : [4, 6, 4, 10]
단, 아무도 근무하지 않을 경우 공평한 것으로 간주

Hash -> <String, int> {name, time}
"""
