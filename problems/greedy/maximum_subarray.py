from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        max_sub = nums[0]
        sub = 0

        for n in nums:
            sub += n
            max_sub = max(max_sub, sub)
            if sub < 0:
                sub = 0

        return max_sub
