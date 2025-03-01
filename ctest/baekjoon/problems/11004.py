# https://www.acmicpc.net/problem/11004 - K번째 수
"""
힙 자료구조는 정렬과 다르다.
heap으로 구성된 후, sort를 하면 자식 노드에서만 정렬이 일어나기 때문에 더 빠를 거라 생각했음
-> 정렬로 바꾸려면 추가적인 비교와 스왑 작업이 필요 O(n log n)

그리고 힙은 [-1]이 최소/최대값을 보장하지 않음. 이 문제는 sort만 써서 푸는 게 나았다.
"""

import heapq

n, k = input().split()
heapq.heapify(heap := [int(i) for i in input().split()])
heap.sort()

print(heap[int(k) - 1])


""" 다른 사람 풀이 
1. 입력 처리 방식, 언패킹(Unpacking)

open(0): 표준 입력(stdin)을 파일 객체처럼 취급
read(): stdin으로부터 모든 데이터를 읽어서 문자열로 반환

*: 변수 언패킹(Unpacking): 리스트나 반복 가능한 객체의 값을 각각의 변수에 할당
e.g 입력 데이터: [4, 1, 2, 3, 5] -> a=4, b=1, x=[2,3,5]
"""
a, b, *x = map(int, open(0).read().split())
print(sorted(x)[b - 1])


""" 다른 사람 풀이 
2. 정렬 알고리즘 - 빠름
"""
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))


def quickSort(A, st, end, K):
    if st < end:
        pivot = partition(A, st, end)
        if pivot == K:  # 분할된 pivot 위치가 K라면 확정
            return
        elif K < pivot:  # K가 pivot보다 왼쪽에 있을 경우
            quickSort(A, st, pivot - 1, K)
        else:  # K가 pivot보다 오른쪽에 있을 경우
            quickSort(A, pivot + 1, end, K)


def partition(A, st, j):

    if st + 1 == j:  # 구간 크기가 2일 경우: 직접 비교 후 정렬
        if A[st] > A[j]:
            A[st], A[j] = A[j], A[st]
        return j

    # 중간값을 pivot으로 선택
    M = (st + j) // 2
    A[st], A[M] = A[M], A[st]
    pivot = A[st]
    i = st + 1

    while i <= j:
        while pivot < A[j] and i <= j:  # 오른쪽 값이 pivot보다 크면 이동
            j = j - 1
        while pivot > A[i] and i <= j:  # 왼쪽 값이 pivot보다 작으면 이동
            i = i + 1
        if i <= j:  # 왼쪽 값이 크고 오른쪽 값이 작다면 교환
            A[i], A[j] = A[j], A[i]
            i = i + 1
            j = j - 1

    A[st] = A[j]  # pivot을 정렬된 위치로 이동
    A[j] = pivot
    return j  # pivot의 최종 위치 반환


quickSort(A, 0, N - 1, K - 1)  # arr, 시작 idx, 끝 idx, k
print(A[K - 1])
