import sys
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        curr_max = nums[0]
        curr_min = nums[0]

        result = nums[0]

        for i in range(1, len(nums)):
            temp = curr_max
            curr_max = max(nums[i], curr_max * nums[i], curr_min * nums[i])
            curr_min = min(nums[i], temp * nums[i], curr_min * nums[i])
            result = max(result, curr_max)

        return result
