from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        back_previous = nums[0]
        previous = max(nums[0], nums[1])
        result = max(back_previous, previous)

        for i in range(2, len(nums)):
            result = max(nums[i] + back_previous, previous)
            back_previous = previous
            previous = result

        return result

    '''
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        # 1 2 3 1
        # 4 1 3 1

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]
    '''

    '''
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
    '''
