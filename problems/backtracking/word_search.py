from typing import List, reveal_type


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        picked = set([])
        def really_exist(row, col, curr) -> bool:
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False

            if (row, col) in picked:
                return False

            if not word.startswith(curr):
                return False

            picked.add((row, col))
            curr += board[row][col]

            if curr == word:
                return True

            exists = (really_exist(row - 1, col, curr) or
            really_exist(row + 1, col, curr) or
            really_exist(row, col - 1, curr) or
            really_exist(row, col + 1, curr))

            picked.discard((row, col))

            return exists

        for r in range(len(board)):
            for c in range(len(board[0])):
                if word.startswith(board[r][c]) and really_exist(r, c, ""):
                    return True

        return False


