import heapq
from collections import deque
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = dict()
        for i in range(1, n + 1):
            graph[i] = []

        for source, nod, t, in times:
            graph[source].append((nod, t))

        def bfs(start):
            visited = set()
            queue = []
            heapq.heapify(queue)
            heapq.heappush(queue, (0, start))

            while queue:
                time, node = heapq.heappop(queue)

                if node in visited:
                    continue

                visited.add(node)

                if len(visited) == n:
                    return time

                for (nei, t) in graph[node]:
                    if nei in visited:
                        continue
                    heapq.heappush(queue, (time + t, nei))

            return -1

        return bfs(k)
