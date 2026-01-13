from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        sub = target - num;
        if sub in seen:
            return [seen[sub], i];
        seen[num] = i;
    return []