# https://school.programmers.co.kr/learn/courses/30/lessons/42626 - 더 맵게
from heapq import heapify, heappop, heappush


# O(NlogN)
def solution(scoville, K):
    # scoville.sort() # O(NlogN)
    # 이후 반복문에서 scoville.pop(0)을 사용할 경우 리스트의 재정렬이 필요하며, 이는 O(N)의 추가 비용을 초래 !!
    heapify(scoville)  # O(N)

    # if not scoville:
    #     return -1

    cnt = 0
    while K > scoville[0]:  # O(N)
        if len(scoville) < 2:
            return -1

        item = heappop(scoville) + (heappop(scoville) * 2)  # O(logN)
        heappush(scoville, item)  # O(logN)
        cnt += 1

    return cnt


# 3항 연산자
def solution(scoville, K):
    heapify(scoville)

    cnt = 0
    while len(scoville) >= 2 and K > scoville[0]:

        item = heappop(scoville) + (heappop(scoville) * 2)
        heappush(scoville, item)
        cnt += 1

    return -1 if scoville[0] < K else cnt


print(solution([1, 2, 3, 9, 10, 12], 7))


# 다른 사람 풀이
"""
queue만 써서 풀었는데도 시간이 heap을 쓴 풀이의 절반 정도 걸리네요. 저는 섞어서 나온 새로운 값, mix들을 별도의 queue에 넣었는데 이게 가장 큰 요인같네요. 나중에 나온 mix값이 먼저 나온 것보다 클 수밖에 없어서 섞는 순서대로 queue에 넣어주면 크기 순서를 신경 쓸 필요가 없어요. 그냥 popleft로 꺼내면 무조건 mix값의 최소입니다
"""
from collections import deque


def solution(scoville, K):
    # 기본 scoville 리스트와 mix 값을 담는 큐
    scoville = deque(sorted(scoville))
    mix_queue = deque()  # 새로운 mix 값을 저장할 큐

    cnt = 0
    while scoville or mix_queue:
        # 두 큐에서 가장 작은 값을 추출
        if mix_queue and (not scoville or mix_queue[0] < scoville[0]):
            first = mix_queue.popleft()
        else:
            first = scoville.popleft()

        if first >= K:
            return cnt

        # 두 번째로 작은 값 추출
        if mix_queue and (not scoville or mix_queue[0] < scoville[0]):
            second = mix_queue.popleft()
        elif scoville:
            second = scoville.popleft()
        else:
            return -1  # 섞을 수 있는 재료가 부족하면 실패

        # 새로운 mix 값 계산 후 mix_queue에 추가
        mix = first + (second * 2)
        mix_queue.append(mix)
        cnt += 1

    return -1
