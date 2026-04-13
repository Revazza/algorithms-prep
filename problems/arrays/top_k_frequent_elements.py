from collections import Counter
from typing import List
import heapq

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    nums_freq = Counter(nums);

    heap = []

    for num, freq in nums_freq.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    result = []
    for freq, num in heap:
        result.append(num)

    return result