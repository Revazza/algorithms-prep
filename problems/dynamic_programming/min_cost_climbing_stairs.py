import sys
from typing import List


class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:

        dp = dict()

        def count_steps(i):
            if i >= len(costs):
                return 0

            if i in dp:
                return dp[i]

            dp[i] = costs[i] + min(
                count_steps(i + 1),
                count_steps(i + 2)
            )

            return dp[i]

        return min(count_steps(0), count_steps(1))
