from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if len(heights) == 0:
            return []

        pacific = set()
        atlantic = set()

        ROW = len(heights)
        COL = len(heights[0])

        def dfs(row, col, visited, prev_height):
            if row < 0 or col < 0 or row == ROW or col == COL or heights[row][col] < prev_height:
                return

            if (row, col) in visited:
                return
            visited.add((row, col))

            dfs(row - 1, col, visited, heights[row][col])
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])

        for r in range(ROW):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COL - 1, atlantic, heights[r][COL - 1])

        for c in range(COL):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROW - 1, c, atlantic, heights[ROW - 1][c])

        result = []
        for r,c in atlantic:
            if (r, c) in pacific:
                result.append([r,c])

        return result