from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        result = []
        queens_positions = []

        def populate(row: int):
            if row == n:
                result.append(generate_board())
                return

            for col in range(n):
                if not queen_position_available(row, col):
                    continue
                queens_positions.append(col)
                populate(row + 1)
                queens_positions.pop()

        def queen_position_available(row: int, col: int) -> bool:
            for queen_row, queen_col in enumerate(queens_positions):
                if queen_col == col:
                    return False
                if abs(row - queen_row) == abs(col - queen_col):
                    return False
            return True

        def generate_board() -> List[str]:
            board = []
            for col in queens_positions:
                row_str = "." * col + "Q" + "." * (n - col - 1)
                board.append(row_str)
            return board

        populate(0)
        return result