import sys
from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        LAND = 2147483647
        WATER = -1
        TREASURE = 0

        def bfs(start_row, start_col)-> int:
            visited = set()
            queue = deque([(start_row, start_col, 0)])

            while queue:
                (row, col, path) = queue.popleft()
                if row < 0 or col < 0 or row == len(grid) or col == len(grid[row]) or grid[row][col] == WATER:
                    continue
                if (row, col) in visited:
                    continue
                if grid[row][col] == LAND:
                    grid[row][col] = path
                if grid[row][col] != LAND and grid[row][col] != TREASURE:
                    grid[row][col] = min(grid[row][col], path)

                visited.add((row, col))

                for dr, dc in directions:
                    queue.append((row + dr, col + dc, path + 1))

            return LAND

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == TREASURE:
                    bfs(r, c)

        return
