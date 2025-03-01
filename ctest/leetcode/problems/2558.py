# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/ - Take Gifts From the Richest Pile
import math
import heapq
from typing import List


# O(n + n + k(log(n) + log(n))) time. -> O(n + k * log(n))
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        gifts = [-i for i in gifts]
        heapq.heapify(gifts)
        # heapq.heapify(gifts := [-i for i in gifts])

        for _ in range(k):
            n = -heapq.heappop(gifts)

            dummy = math.isqrt(n)
            heapq.heappush(gifts, -dummy)
            # heapq.heappush(gifts, -math.isqrt(n))

        return -sum(gifts)


print(Solution().pickGifts([25, 64, 9, 4, 100], 4))


# 다르 사람 풀이
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        i = 0
        while i < k:
            gifts = sorted(gifts)
            sqrt = math.floor(math.sqrt(gifts[-1]))
            gifts[-1] = sqrt
            i += 1
        return sum(gifts)


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            x = max(gifts)
            gifts.remove(x)
            gifts.append(int(math.sqrt(x)))
        return sum(gifts)
