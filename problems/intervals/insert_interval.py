from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = [newInterval]
        def merge(interval1, interval2):
            x01, y01 = interval1
            x02, y02 = interval2
            return [min(x01, x02), max(y01, y02)]

        def add(interval1):
            if overlaps(result[-1], interval1):
                temp = result[-1]
                result.pop()
                result.append(merge(temp, interval1))
            elif result[-1][1] < interval1[0]:
                result.append(interval1)
            else:
                temp = result.pop()
                result.append(interval1)
                result.append(temp)

        def overlaps(interval1, interval2):
            x1, y1 = interval1
            x2, y2 = interval2
            return y1 >= x2 and y2 >= x1

        for interval in intervals:
            add(interval)

        return result