# https://www.acmicpc.net/problem/19638 - 센티와 마법의 뿅망치

import sys
import heapq

input = sys.stdin.readline

N, C, T = map(int, input().split())
heap = []

for _ in range(N):
    h = int(input())
    heapq.heappush(heap, -h)

t = 0  # (T <= 0) 반복문이 실행되지 않으므로, t가 초기화되지 않는 상태 방어
for t in range(1, T + 1):

    # tallest가 C보다 작을 때 or 1
    if -heap[0] < C or -heap[0] == 1:
        t -= 1  # 뿅망치 사용 X
        break

    h = heapq.heappop(heap)
    heapq.heappush(heap, -(-h // 2))

if C == 1 or -heap[0] >= C:
    print(f"NO\n{-heap[0]}")
else:
    print(f"YES\n{t}")


""" 원래 생각했던 것 ㅜ,ㅜ
while 문으로 tallest가 C보다 작아질 때 까지 반복 -> 넣고 빼고 복잡해짐 (시간 짱오래 걸림) => T를 기준으로 잡아야...
heappop 으로 꺼내서 비교 -> 다시 힙에 추가해야 하는 경우가 생김 (이 부분 빼먹음) => heap[0] 으로 할 것
T가 0이되면 break, 조건처리
"""
