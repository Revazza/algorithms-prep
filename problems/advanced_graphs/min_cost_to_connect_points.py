import heapq
import sys
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if len(points) == 0:
            return 0

        graph = dict()
        for xi,yi in points:
            graph[(xi, yi)] = []

        for xi, yi in points:
            for xj, yj in points:
                if xj == xi and yj == yi:
                    continue
                cost = abs(xi - xj) + abs(yi - yj)
                graph[(xi, yi)].append((xj, yj, cost))

        def prim(point):
            point_x, point_y = point
            visited = set()
            queue = []
            heapq.heapify(queue)
            heapq.heappush(queue, (0, point_x, point_y))
            total = 0

            while queue:
                c, x, y = heapq.heappop(queue)

                if (x, y) in visited:
                    continue

                visited.add((x, y))
                total += c
                if len(visited) == len(points):
                    return total

                for xy, yj, xycost in graph[(x, y)]:
                    if (xy, yj) in visited:
                        continue
                    heapq.heappush(queue, (xycost, xy, yj))

            return total

        return prim(points[0])
