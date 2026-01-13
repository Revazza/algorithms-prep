from collections import Counter
from typing import List

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = Counter(nums);
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse = True);
    return [x[0] for x in sorted_count[:k]];