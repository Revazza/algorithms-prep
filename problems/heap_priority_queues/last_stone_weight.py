import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones = [2,3,6,2,4]
        # heap_stones = [6,4,3,2,2]

        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)

            div = abs(stone1 - stone2)
            if div == 0:
                continue
            heapq.heappush(heap, -div)


        return -heap[0] if len(heap) == 1 else 0
