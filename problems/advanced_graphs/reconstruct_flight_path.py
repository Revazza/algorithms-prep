import heapq
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = dict()
        for src, dest in tickets:
            adj[src] = []

        tickets.sort()

        for src, dest in tickets:
            adj[src].append(dest)

        result = ["JFK"]

        def dfs(node):
            if len(result) == len(tickets) + 1:
                return True
            if node not in adj:
                return False

            temp = list(adj[node])
            for i, v in enumerate(temp):
                result.append(v)
                adj[node].pop(i)

                if dfs(v):
                    return True

                result.pop()
                adj[node].insert(i,v)

            return False

        dfs("JFK")
        return result
