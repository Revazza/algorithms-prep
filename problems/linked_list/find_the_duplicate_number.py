from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]

        return 1
