import sys
from typing import List


class Solution:


    '''
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if len(matrix) == 0:
            return 0

        dir = [[-1,0],[1,0],[0,1],[0,-1]]
        cache = {}
        ROW = len(matrix)
        COL = len(matrix[0])

        def dfs(row, col):
            if (row, col) in cache:
                return cache[(row,col)]

            best = 1
            for dr, dc in dir:
                nr = row + dr
                nc = col + dc
                if (0 <= nr < ROW and 0 <= nc < COL and matrix[row][col] > matrix[nr][nc]):
                    best = max(best, 1 + dfs(nr, nc))

            cache[(row, col)] = best
            return best

        ways = 0
        for r in range(ROW):
            for c in range(COL):
                ways = max(ways, dfs(r, c))

        return ways
    '''
