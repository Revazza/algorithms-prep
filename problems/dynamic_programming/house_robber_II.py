from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.rob_house(nums[1:]), self.rob_house(nums[:-1]))

    def rob_house(self, nums):
        rob1 = 0
        rob2 = 0

        for n in nums:
            result = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = result

        return rob2


    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_house(i, max_i, dp):
            if i >= max_i:
                return 0

            if i in dp:
                return dp[i]

            dp[i] = max(nums[i] + rob_house(i + 2, max_i, dp), rob_house(i + 1, max_i, dp))

            return dp[i]

        return max(rob_house(0, len(nums) - 1,dict()), rob_house(1, len(nums), dict()))
    '''