from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        # Time Complexity O(n)
        # Space Complexity O(n)
        max_left = [0] * len(heights)
        curr_max = heights[0];
        # [0,2,0,3,1,0,1,3,2,1]
        #  0 0 2 2 3 3 3 3 3 3
        for i in range(1, len(heights)):
            max_left[i] = curr_max
            curr_max = max(curr_max, heights[i])

        max_right = [0] * len(heights)
        curr_max = heights[len(heights) - 1]

        # [0,2,0,3,1,0,1,3,2,1]
        #  3 3 3 3 3 3 3 2 1 0

        for i in range(len(heights) - 1, -1, -1):
            max_right[i] = curr_max
            curr_max = max(curr_max, heights[i])

        result = 0

        for i in range(len(heights)):
            trapped_water = max(min(max_left[i], max_right[i]) - heights[i], 0)
            result += trapped_water

        return result
