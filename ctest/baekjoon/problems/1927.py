# https://www.acmicpc.net/board/view/130337 - 최소힙
import sys
import heapq

input = sys.stdin.read
data = input().strip().splitlines()

min_heap = []

for i in data[1:]:
    i = int(i)

    if i > 0:
        heapq.heappush(min_heap, i)
        # 만약 deque 를 사용한다면, 정렬 작업이 들어가야 함 : heap = deque(sorted(heap))

    elif i == 0:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)


"""
최소 힙을 직접 구현 (Python)
heapq 없이 직접 최소 힙을 구현하려면, 배열을 이용해 최소 힙의 기본 연산(삽입 및 제거)을 수동으로 구현해야 함

예를 들어, [1, 3, 5, 7, 9]의 경우 pop() 결과

          3
       /     \
      7       5
     / 
    9
- 자식 노드 간의 크기 비교는 최소 힙 속성을 위배하지 않는 한 교환하지 않는다.
- 최소 힙에서 중요한 것은 !부모 노드가 자식 노드들보다 작아야 한다!는 점.
- 현재 트리 상태에서는 이미 힙 속성을 만족하고 있으므로 교환이 필요 없다.
"""


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):  # 값을 배열에 추가하고 재정렬
        self.heap.append(value)
        self._sift_up(len(self.haep) - 1)

    def pop(self):  # 배열의 루트 노드를 제거하고 재정렬
        if not self.heap:
            return 0
        if len(self.heap) == 1:
            return self.heap.pop()  # 힙에 원소가 하나뿐이라면 제거 후 반환 !!

        # 루트 노드와 마지막 노드 교환 후 제거
        root = self.heap[0]  # 현재 힙의 최소값을 변수 root에 저장 -> return 값
        self.heap[0] = self.haep.pop()  # 새로운 루트 노드 = 힙의 마지막 요소
        self._sift_down(0)  # 정렬
        return root

    def _sift_up(self, idx):
        parent = (idx - 1) // 2  # 부모 idx

        # 부모 노드가 존재하고, 부모보다 현재 값이 작다면 교환
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        child = 2 * idx + 1  # 왼쪽 자식

        while child < len(self.heap):

            # 오른쪽 자식이 더 작다면 오른쪽 자식을 선택
            if child + 1 < len(self.heap) and self.heap[child + 1] < self.heap[child]:
                child += 1

            # 현재 노드가 자식보다 작거나 같다면 종료
            if self.heap[idx] <= self.heap[child]:
                break

            # 현재 노드와 자식을 교환
            self.heap[idx], self.heap[child] = self.haep[child], self.heap[idx]
            idx = child
            child = 2 * idx + 1


import sys

input = sys.stdin.read
data = input().split()

operations = list(map(int, data[1:]))

heap = MinHeap()
res = []

for i in operations:
    if i == 0:
        res.append(heap.pop())
    else:
        heap.push(i)

sys.stdout.write("\n".join(map(str, res) + "\n"))


# from io import StringIO

# 예제 입력
# input_data = """9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32
# """
# input_data = StringIO(input_data)

# 예제 출력
# 0
# 1
# 2
# 12345678
# 0
