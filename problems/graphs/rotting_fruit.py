from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        fresh_count = 0
        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == FRESH:
                    fresh_count += 1
                elif grid[r][c] == ROTTEN:
                    queue.append((r, c))


        rotten_count = len(queue)
        total = rotten_count + fresh_count
        time = 0

        def add_to_queue(o_row, o_col) -> int:
            if (o_row < 0 or o_col < 0 or o_row == len(grid) or o_col == len(grid[o_row]) or
                    grid[o_row][o_col] == EMPTY or grid[o_row][o_col] == ROTTEN):
                return 0

            grid[o_row][o_col] = ROTTEN
            queue.append((o_row, o_col))
            return 1

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                rotten_count += add_to_queue(row + 1, col)
                rotten_count += add_to_queue(row - 1, col)
                rotten_count += add_to_queue(row, col + 1)
                rotten_count += add_to_queue(row, col - 1)

            time += 1

        time = max(time - 1, 0)

        return time if rotten_count == total else -1

