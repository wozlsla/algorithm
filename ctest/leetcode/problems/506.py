# https://leetcode.com/problems/relative-ranks/description/ - 506.Relative Ranks
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        ranks = []
        for i, s in enumerate(score):
            ranks.append([s, i])

        ranks.sort(reverse=True)  # idx: 순위
        # [[10, 0], [9, 3], [8, 2], [4, 4], [3, 1]]

        for i, rank in enumerate(ranks):
            if i == 0:
                rank[0] = "Gold Medal"
            elif i == 1:
                rank[0] = "Silver Medal"
            elif i == 2:
                rank[0] = "Bronze Medal"
            else:
                rank[0] = str(i + 1)  # (rank, idx)

        res = [item[0] for item in sorted(ranks, key=lambda x: x[1])]

        return res


score = [5, 4, 3, 2, 1]
score = [10, 3, 8, 9, 4]
print(Solution().findRelativeRanks(score))


# 다른 사람 풀이
# priority queue
# https://leetcode.com/problems/relative-ranks/solutions/5127969/faster-less-mem-3-methods-detailed-approach-sorting-heap-map-python-java-c/
import heapq


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)

        # Create a heap of pairs (score, index)
        heap = []
        for index, score in enumerate(score):
            heapq.heappush(heap, (-score, index))

        # Assign ranks to athletes
        rank = [0] * N  # 이렇게 하면 되는군..
        place = 1
        while heap:
            original_index = heapq.heappop(heap)[1]
            if place == 1:
                rank[original_index] = "Gold Medal"
            elif place == 2:
                rank[original_index] = "Silver Medal"
            elif place == 3:
                rank[original_index] = "Bronze Medal"
            else:
                rank[original_index] = str(place)
            place += 1

        return rank


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank_mapping = {
            score: medals[i] if i < 3 else str(i + 1)
            for i, score in enumerate(sorted_score)
        }
        return [rank_mapping[score] for score in score]


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = {}
        res = []
        descScore = sorted(score, reverse=True)

        for i in range(len(descScore)):
            if i == 0:
                d[descScore[i]] = "Gold Medal"
            elif i == 1:
                d[descScore[i]] = "Silver Medal"
            elif i == 2:
                d[descScore[i]] = "Bronze Medal"
            else:
                d[descScore[i]] = str(i + 1)

        for i in range(len(score)):
            res.append(d[score[i]])

        return res
