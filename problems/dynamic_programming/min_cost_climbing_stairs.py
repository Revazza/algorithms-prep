import sys
from typing import List


class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:

        cache = {}

        def calc_cost(i):
            if i >= len(costs):
                return 0

            if i in cache:
                return cache[i]

            cache[i] = costs[i] + min(
                calc_cost(i + 1),
                calc_cost(i + 2)
            )

            return cache[i]

        return min(calc_cost(0), calc_cost(1))
