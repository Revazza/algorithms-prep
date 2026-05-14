from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        subset = []

        def gather(i):
            if i == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])
            gather(i + 1)

            subset.pop()
            gather(i + 1)

        gather(0)
        return result
