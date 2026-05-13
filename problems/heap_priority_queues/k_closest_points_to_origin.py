import heapq
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        heapq.heapify(heap)

        for coordinate in points:
            x = coordinate[0]
            y = coordinate[1]
            distance = sqrt(x**2 + y**2)

            heapq.heappush(heap,(distance, [x, y]))

        return [heapq.heappop(heap)[1] for _ in range(k)]
