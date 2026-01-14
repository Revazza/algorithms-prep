from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    if len(nums) == 0:
        return []

    # 3  5  2   8
    # 80 48 120 30

    # 3  5  2  8

    # 1  3  15 30
    # 80 16 8  1
    #

    left = [1] * len(nums);

    i = 1;

    while i < len(nums):
        prev_left = left[i - 1]
        left[i] = prev_left * nums[i - 1]
        i += 1;

    right = [1] * len(nums)

    i = len(right) - 2;

    while i >= 0:
        prev_right = right[i + 1];
        right[i] = prev_right * nums[i + 1]
        i -= 1;

    result = []
    i = 0;
    while i < len(nums):
        result.append(left[i] * right[i])
        i += 1;

    return result