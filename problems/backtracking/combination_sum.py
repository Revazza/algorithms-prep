from typing import List, Counter


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # [2,5,6,9]

        nums.sort()
        result = []
        sets = []

        def find_sums(start, total):
            if total == target:
                result.append(sets.copy())
                return

            for i in range(start, len(nums)):
                if total + nums[i] > target:
                    return
                sets.append(nums[i])
                find_sums(i, total + nums[i])
                sets.pop()

        find_sums(0, 0)
        return result
