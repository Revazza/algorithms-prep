from collections import defaultdict
from typing import List

def threeSum(self, nums: List[int]) -> List[List[int]]:

    # Time Complexity O(n^2)
    # Space Complexity O(n) -> O(n^2) worst
    target = 0
    nums.sort()
    triplets = set()

    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1

        while l < r:
            if nums[l] + nums[r] + nums[i] > target:
                r -= 1
            elif nums[l] + nums[r] + nums[i] < target:
                l += 1
            else:
                triplets.add(tuple([nums[i], nums[l], nums[r]]))
                l += 1
                r -= 1

    return [list(t) for t in triplets]


def threeSumOptimized(self, nums: List[int]) -> List[List[int]]:

    target = 0
    nums.sort()
    triplets = set()

    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1

        while l < r:
            if nums[l] + nums[r] + nums[i] > target:
                r -= 1
            elif nums[l] + nums[r] + nums[i] < target:
                l += 1
            else:
                triplets.add(tuple([nums[i], nums[l], nums[r]]))
                l += 1
                r -= 1

    return [list(t) for t in triplets]

