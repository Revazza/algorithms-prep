from typing import List, Counter


class Solution:from typing import List, Counter


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # 1,2,2,3
        nums.sort()
        result = []
        subset = []
        def gather(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])
            gather(i + 1)

            num = subset.pop()
            while i + 1 < len(nums) and nums[i + 1] == num:
                i += 1
            gather(i + 1)

        gather(0)
        return result