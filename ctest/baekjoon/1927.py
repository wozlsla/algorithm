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
