from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = dict()

        def rob_house(i):
            if i >= len(nums):
                return 0

            if i in dp:
                return dp[i]

            robbed = nums[i] + rob_house(i + 2)
            not_robbed = rob_house(i + 1)

            dp[i] = max(robbed, not_robbed)

            return dp[i]

        return rob_house(0)
