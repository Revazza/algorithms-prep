from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        # [0,1,2]
        # [1,2,0]
        # [2,0,1]
        # 5,1,2,3,4
        # target=1


        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1