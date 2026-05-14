from typing import List, Counter


class Solution:from typing import List, Counter


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []
        subset = []
        cache = set([])
        def gather(i):
            if i == len(nums):
                count = tuple(sorted(Counter(subset).items()))
                if count in cache:
                    return
                result.append(subset.copy())
                cache.add(count)
                return

            subset.append(nums[i])
            gather(i + 1)

            subset.pop()
            gather(i + 1)

        gather(0)
        return result