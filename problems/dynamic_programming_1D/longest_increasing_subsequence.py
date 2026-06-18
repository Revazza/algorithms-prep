from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp = {i: 1 for i in range(len(nums))}

        max_length = 1

        for i in range(len(nums) - 1, -1, -1):
            temp_length = 1
            for j in range(i + 1, len(nums)):
                if nums[i] >= nums[j]:
                    continue
                temp_length = max(temp_length, 1 + dp[j])

            max_length = max(temp_length, max_length)
            dp[i] = temp_length

        return max_length
