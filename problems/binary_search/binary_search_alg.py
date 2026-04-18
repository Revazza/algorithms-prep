from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # -1,0,2,4,6,8   4
        #
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (right + left) // 2

            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return -1;
