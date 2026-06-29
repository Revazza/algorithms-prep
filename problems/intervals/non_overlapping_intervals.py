from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # [[1,2],[2,4],[1,4]]
        # [[1,2],[1,4],[2,4]] -> [[1,2]]

        intervals.sort()
        last = intervals[0]
        erased = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < last[1]:
                last = [last[0], min(last[1], end)]
                erased += 1
            else:
                last = [start, end]

        return erased