from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        combination = []
        used = set([])

        def gather():
            if len(combination) == len(nums):
                result.append(combination.copy())
                return

            for i in range(0, len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                combination.append(nums[i])
                gather()
                used.remove(nums[i])
                combination.pop()



        gather()
        return result
