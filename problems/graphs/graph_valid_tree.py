from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        graph = dict()
        for i in range(n):
            graph[i] = []
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def all_reachable(node, parent) -> bool:
            if node in visited:
                return False
            visited.add(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour == parent:
                    continue
                if not all_reachable(neighbour, node):
                    return False
            return True

        return all_reachable(0, -1) and len(visited) == n