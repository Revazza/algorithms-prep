from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        def dfs(row, col):
            if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]):
                return

            if (row,col) in visited:
                return

            if grid[row][col] != '1':
                return

            visited.add((row, col))

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

            return

        islands = 0;

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands
