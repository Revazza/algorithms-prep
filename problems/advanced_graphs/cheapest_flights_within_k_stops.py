import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], source: int, dst: int, k: int) -> int:
        # Bellman ford -
        # This solution is not correct
        adj = dict()
        for i in range(n):
            adj[i] = []

        for flight_from, flight_to, flight_price in flights:
            adj[flight_from].append((flight_to, flight_price))

        queue = []
        heapq.heapify(queue)
        heapq.heappush(queue, (0, source, 0))

        visited = set()

        while queue:
            cost, src, flight_count = heapq.heappop(queue)

            if flight_count - 1 > k:
                continue

            if src in visited:
                continue

            if src == dst:
                return cost

            visited.add(src)

            for nei, price in adj[src]:
                if nei in visited:
                    continue

                heapq.heappush(queue, ((cost + price), nei, flight_count + 1))


        return -1
