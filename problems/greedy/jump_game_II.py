from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        l = 0
        r = 0
        jumps = 0
        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, r + nums[i])
            l = r + 1
            r = furthest
            jumps += 1

        return jumps
