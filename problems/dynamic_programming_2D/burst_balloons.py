from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        def calc(i):
            if i == len(nums):
                return 0



            return

        def calcBurst(i, bursted):

            prod = nums[i]

            for l in range(i - 1, -1, -1):
                if l not in bursted:
                    prod *= nums[l]
                    break

            for r in range(i + 1, len(nums)):
                if r not in bursted:
                    prod *= nums[r]
                    break

            return prod

        return calc(set())
