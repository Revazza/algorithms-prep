"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) == 0:
            return True

        intervals.sort(key=lambda x: x.start)

        last = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]

            if last.end > interval.start:
                return False
            last = interval

        return True
