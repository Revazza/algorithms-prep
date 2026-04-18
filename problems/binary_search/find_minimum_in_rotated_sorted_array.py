import sys
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1
        min_val = sys.maxsize
        #  [3,4,5,6,1,2]
        while left <= right:
            mid = (right + left) // 2

            min_val = min(nums[mid], min_val)

            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return min_val