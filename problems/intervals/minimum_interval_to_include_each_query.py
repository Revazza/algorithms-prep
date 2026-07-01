import heapq
import sys
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()
        queries.sort()

        result = []
        minHeap = []
        heapq.heapify(minHeap)

        for q in queries:

            for start, end in intervals:
                if start > q:
                    break
                heapq.heappush(minHeap, (end - start + 1, end))



        return []

    '''
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        result = []

        for query in queries:

            min_length = sys.maxsize
            for start, end in intervals:
                if start <= query <= end:
                    min_length = min(min_length, end - start + 1)
            if min_length == sys.maxsize:
                min_length = -1

            result.append(min_length)

        return result
    '''