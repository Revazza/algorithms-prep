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
    triplets = []

    #Input: nums = [-1, 0, 1, 2, -1, -4]

    # sorted - [-4, -1, -1, 0, 1 , 2]

    #Output: [[-1, -1, 2], [-1, 0, 1]]

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1

        while l < r:
            if nums[i] + nums[l] + nums[r] > target:
                r -= 1
            elif nums[i] + nums[l] + nums[r] < target:
                l += 1
            else:
                triplets.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return triplets


