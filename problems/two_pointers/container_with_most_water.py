from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Time Complexity O(n)
        # Space Complexity O(1)
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            width = r - l
            max_area = max(max_area, min(heights[l], heights[r]) * width)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
