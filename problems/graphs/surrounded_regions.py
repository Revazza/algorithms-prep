from operator import and_
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if len(board) == 0:
            return

        ROW = len(board)
        COL = len(board[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row == ROW or col == COL or board[row][col] != 'O':
                return

            board[row][col] = 'T'
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for r in range(ROW):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][COL - 1] == 'O':
                dfs(r,COL - 1)

        for c in range(COL):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROW - 1][c] == 'O':
                dfs(ROW - 1, c)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'


        return
