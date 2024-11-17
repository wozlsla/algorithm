# https://www.acmicpc.net/problem/2075 - N번째 큰 수
# wozlsla.notion.site/141d382c218d808aa69df0896dcfba40

import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):  # 한 줄씩 받음 -> 계속 받을 수 있게 설계해야 함
    nums = list(map(int, input().split()))
    for num in nums:
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappop(heap)  # 정렬 1
                heapq.heappush(heap, num)  # 정렬 2
                # heapq.heappushpop(heap, num) - 새로운 값을 힙에 추가한 다음, 힙에서 최솟값을 제거 - 한번만 재정렬
print(heap[0])

# print(heap)
# [35, 41, 48, 52, 49]
# heappushpop의 경우 : [35, 41, 48, 49, 52]

# 최소 힙의 조건 : 각 부모 노드의 값이 자식 노드의 값보다 작거나 같으면 조건을 만족
# 배열의 요소 순서는 다를 수 있지만, 힙 속성을 만족하면 올바른 최소 힙이라고 할 수 있다


""" 다른 사람 풀이
1. 처음 n개의 숫자를 힙에 추가하고 heapify로 초기 힙 구성
2. heapreplace: 힙의 최솟값을 새로운 숫자로 대체하고, 힙의 속성을 유지 (정렬)

힙의 크기를 N으로 일정하게 유지하면서, 새로운 숫자가 힙의 최솟값보다 클 경우에만 힙을 갱신하기 때문에
이 문제에서는 셋 중 가장 빠른 해법
"""
input = sys.stdin.readline


def main():
    n = int(input())
    heap = list(map(int, input().split()))
    heapq.heapify(heap)

    for _ in range(n - 1):
        nums = map(int, input().split())
        for num in nums:
            if num > heap[0]:
                heapq.heapreplace(heap, num)

    print(heap[0])


main()
