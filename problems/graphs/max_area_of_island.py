from typing import List


class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(row, col):
            if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(row + dr, col + dc)

            return area

        max_area = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                scope_area = dfs(r, c)
                max_area = max(max_area, scope_area)

        return max_area