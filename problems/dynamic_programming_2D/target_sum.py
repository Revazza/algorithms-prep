from collections import defaultdict
from typing import List


class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(len(nums)):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count

        return dp[len(nums)][target]

    '''
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache = {}

        def calc(i, amount):
            if i == len(nums):
                if amount == target:
                    return 1
                return 0

            if (i, amount) in cache:
                return cache[(i, amount)]

            ways = 0

            ways += calc(i + 1, amount - nums[i])
            ways += calc(i + 1, amount + nums[i])

            cache[(i, amount)] = ways

            return ways

        return calc(0, 0)
    '''