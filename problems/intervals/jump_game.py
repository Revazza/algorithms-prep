from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:

        post = len(nums) - 1

        for r in range(len(nums) - 1, -1, -1):
            if r + nums[r] >= post:
                post = r

        return nums[0] >= post

    '''
    def canJump(self, nums: List[int]) -> bool:

        cache = {}
        def canReallyJump(i):
            if i + nums[i] >= len(nums) - 1:
                return True

            if i in cache:
                return cache[i]

            jumps = nums[i]

            while jumps != 0:
                if canReallyJump(i + jumps):
                    return True

                jumps -= 1

            cache[i] = False

            return False


        return canReallyJump(0)
    '''