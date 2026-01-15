from typing import List


def twoSum(self, numbers: List[int], target: int) -> List[int]:

    # Time Complexity O(n^2)
    # Space Complexity O(1)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

    return []

def twoSumOptimized(self, nums: List[int], target: int) -> List[int]:

    # Time Complexity O(n)
    # Space Complexity O(1)
    l = 0;
    r = len(nums)

    while l < r:
        if nums[l] + nums[r] == target:
            return [l + 1, r + 1]

        if nums[l] + nums[r] > target:
            r -= 1

        if nums[l] + nums[r] < target:
            l += 1

    return []