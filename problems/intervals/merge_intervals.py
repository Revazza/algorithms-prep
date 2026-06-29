from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def overlaps(interval1, interval2):
            x1, y1 = interval1
            x2, y2 = interval2
            return y1 >= x2 and y2 >= x1

        def merge(interval1, interval2):
            return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

        if len(intervals) == 0:
            return []

        intervals.sort()

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if not overlaps(result[-1], interval):
                result.append(interval)
                continue

            result.append(merge(result.pop(), interval))

        return result
