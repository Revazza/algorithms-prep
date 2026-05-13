import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # [2,3,1,5,4], k = 2
        # [-5,-4,-3,-2,-1]
        heap = [-x for x in nums]
        heapq.heapify(heap)

        while k > 1:
            heapq.heappop(heap)
            k -= 1

        return -heap[0]
