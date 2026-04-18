from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_p = 0

        stack = []

        for i in range(len(heights)):
            max_p = max(heights[i], max_p)

            while stack and heights[stack[-1]] >= heights[i]:
                curr_max = heights[stack[-1]] * (i - stack[-1])
                max_p = max(curr_max, max_p)
                stack.pop()

            stack.append(i)

        return max_p
