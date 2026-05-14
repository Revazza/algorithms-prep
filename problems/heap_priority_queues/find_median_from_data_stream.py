import heapq


class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

        heapq.heapify(self.low)
        heapq.heapify(self.high)
        return

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)

        if len(self.low) > len(self.high) + 1:
            low = -heapq.heappop(self.low)
            heapq.heappush(self.high, low)

        if self.high and -self.low[0] > self.high[0]:
            high = heapq.heappop(self.high)
            low = -heapq.heappop(self.low)
            heapq.heappush(self.low, -high)
            heapq.heappush(self.high, low)

        if len(self.high) > len(self.low) + 1:
            high = heapq.heappop(self.high)
            heapq.heappush(self.low, -high)

        return None
    def findMedian(self) -> float:

        if (len(self.low) +len(self.high)) % 2 == 0:
            return (-self.low[0] + self.high[0]) / 2

        return -self.low[0]

