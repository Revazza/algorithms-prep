"""
Definition of Interval:
"""
from encodings.rot_13 import rot13_map
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:

    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)

        i, k = 0, 0

        rooms = 0
        count = 0
        while i < len(intervals):

            if starts[i] < ends[k]:
                i += 1
                count += 1
            else:
                count -= 1
                k += 1

            rooms = max(rooms, count)

        return rooms

    '''
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # This solution doesn't work but still I like it
        def overlaps(interval1, interval2):
            return interval1.end >= interval2.start and interval2.end >= interval1.start

        def merge(interval1, interval2):
            return Interval(
                min(interval1.start, interval2.start),
                max(interval1.end, interval2.end),
            )

        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x.start)

        meetings = []

        for i in range(len(intervals)):
            interval = intervals[i]
            merged = False

            for k in range(len(meetings)):
                if overlaps(interval, meetings[k]):
                    meetings[k] = merge(interval, meetings[k])
                    merged = True
                    break

            if not merged:
                meetings.append(interval)

        return len(meetings)
    '''