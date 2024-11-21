# https://www.acmicpc.net/problem/1417 - 국회의원 선거
import sys
from heapq import heapify, heappop, heappush


lines = sys.stdin.read().strip().splitlines()

std = int(lines[1])
heapify(votes := [-int(i) for i in lines[2:]])

cnt = 0
while std and std <= -votes[0]:  # 후보가 없는 경우도 고려해야 함
    top = -heappop(votes)
    std += 1
    cnt += 1
    heappush(votes, -(top - 1))

print(cnt)

# 1. 빈 heap 에 인덱스로 접근
# heap[0] - IndexError: list index out of range


# 다른 사람 풀이
# index (혹은 sort) 사용, 불필요 연산 제거
N = int(input())
candidates = [int(input()) for i in range(N)]

std = candidates[0]
votes = candidates[1:]

cnt = 0
while votes and std <= max(votes):
    idx = votes.index(max(votes))
    votes[idx] -= 1
    std += 1
    cnt += 1
    if std > max(votes):  # std가 최댓값이라면 반복을 중단
        break
print(cnt)
