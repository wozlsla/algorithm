n = int(input())  # week

schedule = {}

for _ in range(n):
    for i in range(4):
        shift = input().split()
        time = [4, 6, 4, 10][i]

        for worker in shift:
            if worker == "-":
                continue
            schedule.setdefault(worker, 0)
            schedule[worker] += time

work = schedule.values()
if not work:
    print("Yes")
elif max(work) - min(work) <= 12:
    print("Yes")
else:
    print("No")


""" 2
dict.setdefault(x, 0) : 키 x가 없으면 0을 기본값으로 설정. 키가 이미 존재하면 아무 동작을 하지 않고 값을 반환.
work.get(x, 0) : 키가 없을 때 기본값을 반환하지만, 딕셔너리를 직접 수정하지는 않는다.
"""
import sys

# input() 함수를 sys.stdin.readline()을 이용해 재정의
input = lambda: sys.stdin.readline().strip("\n")

n = int(input())
schedule = {}

for _ in range(n):
    for time in [4, 6, 4, 10]:
        shift = input().split()

        for worker in shift:
            if worker == "-":
                continue
            schedule[worker] = schedule.get(worker, 0) + time

if not schedule:
    print("Yes")
elif max(schedule.values()) - min(schedule.values()) <= 12:
    print("Yes")
else:
    print("No")
