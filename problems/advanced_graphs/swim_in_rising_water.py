import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        queue = []
        heapq.heapify(queue)
        heapq.heappush(queue, (grid[0][0], 0, 0))

        visited = set()
        visited.add((0, 0))

        while queue:
            time, row, col = heapq.heappop(queue)


            if row == len(grid) - 1 and col == len(grid) - 1:
                return max(time, grid[row][col])

            self.add_to_queue(row - 1, col, time, queue, grid, visited)
            self.add_to_queue(row + 1, col, time, queue, grid, visited)
            self.add_to_queue(row, col - 1, time, queue, grid, visited)
            self.add_to_queue(row, col + 1, time, queue, grid, visited)

        return 0

    def add_to_queue(self, row, col, time, queue, grid, visited):
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[row]):
            return
        if (row, col) in visited:
            return

        time = max(time, grid[row][col])
        heapq.heappush(queue, (time, row, col))
        visited.add((row, col))
