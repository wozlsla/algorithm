# https://leetcode.com/problems/delete-greatest-value-in-each-row/description/ - Delete Greatest Value in Each Row
from typing import List
from heapq import heapify, heappop, heappush


# O(m * n log n)
# 큰 입력 크기에서는 max와 remove는 비효율적
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = []
        # res = 0

        while len(grid[0]):  # 각 열의 개수만큼 반복
            heapify(heap := [])
            for row in grid:  # 각 행마다 반복
                val = max(row)  # O(M) (행 길이만큼 탐색)
                heappush(heap, -val)  # O(log(N)) (최대힙 삽입)
                row.remove(val)  # O(M) (값 제거)
            res.append(-heappop(heap))  # O(log(N)) (최대힙 삭제)
            # res += -heappop(heap)

        return sum(res)


grid = [[1, 2, 4], [3, 3, 1]]
grid = [[10]]
print(Solution().deleteGreatestValue(grid))


# 다른 사람 풀이
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        for row in grid:
            row.sort()

        # Transpose the grid to get columns O(M⋅N)
        tp = zip(*grid)

        return sum(max(col) for col in tp)
        # return sum(max(col) for col in zip(*grid))
