# https://school.programmers.co.kr/learn/courses/30/lessons/42628?language=python3 - 이중우선순위큐
from heapq import heappop, heappush


def solution(operations):
    cnt = []

    for oper in operations:
        cmd, value = oper.split()

        if cmd == "I":
            heappush(cnt, int(value))
        elif not cnt:
            continue
        else:
            if value == "1":
                cnt.remove(max(cnt))
                # del cnt[-1]
            else:
                heappop(cnt)

    return [0, 0] if not cnt else [max(cnt), min(cnt)]
    # return [cnt[-1], cnt[0]]


# 힙 구조에서 최댓값은 cnt[-1]에 항상 위치하지 않을 수 있다 !!

arr = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
arr = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
arr = ["I 7", "I 7", "I 7", "I 7", "D 1", "D -1"]
print(solution(arr))


"""
반례 : arr = ["I 6", "I 2", "I 1", "I 4", "I 5", "I 3", "D 1", "I 7", "D -1", "I 6", "D -1", "D -1"]  7,4
max가 리프 노드에 있다는 것은 보장되지만 가장 끝 노드(인덱스)에 있다는 것은 보장되지 않는다. 
즉, remove로 제거해버리면 heap 구조가 깨질 수 있음
+ 저렇게 삭제를 한다면 해당 리프의 뒤에 있던 원소들이 앞으로 끌려와서 트리가 깨질 수 있음
remove 이후 heapify를 써서 다시 만들어주거나 해야 함..

2) sort, heappop, pop 이용 할 수도 있음
"""


# GPT
def solution(operations):
    min_heap = [] 
    max_heap = []
    element_count = {}  # 각 숫자의 삽입 횟수를 기록

    for operation in operations:
        cmd, value = operation.split()
        value = int(value)

        if cmd == "I":
            heappush(min_heap, value)
            heappush(max_heap, -value)
            # 삽입 횟수 기록
            if value in element_count:
                element_count[value] += 1
            else:
                element_count[value] = 1

        elif cmd == "D":
            if not min_heap or not max_heap:
                continue

            if value == 1:  # 최댓값 삭제
                while max_heap:
                    max_val = -heappop(max_heap)  # 최대 힙에서 최댓값 꺼냄
                    if element_count.get(max_val, 0) > 0:  # 유효한 값인지 확인 (최소 힙에서 제거된 값일 수 있기 때문)
                        element_count[max_val] -= 1  # 삭제 처리
                        break

            elif value == -1:  # 최솟값 삭제
                while min_heap:
                    min_val = heappop(min_heap)
                    if element_count.get(min_val, 0) > 0:  
                        element_count[min_val] -= 1 
                        break

    # 최종 남아 있는 유효한 값 찾기
    while min_heap and element_count.get(min_heap[0], 0) == 0:
        heappop(min_heap)  # 유효하지 않은 값 제거

    while max_heap and element_count.get(-max_heap[0], 0) == 0:
        heappop(max_heap)


    if not min_heap or not max_heap:  
        return [0, 0]

    return [-max_heap[0], min_heap[0]] 



arr = ["I 6", "I 2", "I 1", "I 4", "I 5", "I 3", "D 1", "I 7", "D -1", "I 6", "D -1", "D -1"]
arr = ["I 7", "I 7", "I 7", "I 7", "D 1", "D -1"]
arr = ["I 5", "I 3", "I 5", "D 1", "D 1"] # 3
print(solution(arr))















