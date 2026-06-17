from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        total_sum = sum(nums)

        def canItReally(curr_index, total):
            if total_sum / 2 == total:
                return True

            if curr_index == len(nums):
                return False

            return (canItReally(curr_index + 1, total + nums[curr_index]) or
                    canItReally(curr_index + 1, total))

        return canItReally(0, 0)
