from typing import List


def hasDuplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums));