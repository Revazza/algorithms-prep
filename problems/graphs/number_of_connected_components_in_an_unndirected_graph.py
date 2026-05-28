from typing import List


class Solution:
    def countComponents(self, some_N: int, edges: List[List[int]]) -> int:
        graph = dict()
        for i in range(some_N):
            graph[i] = []

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()

        def dfs(start_node) -> int:
            if start_node in seen:
                return 0
            stack = [start_node]

            while stack:
                node = stack.pop()
                seen.add(node)
                neighs = graph[node]

                for nei in neighs:
                    if nei in seen:
                        continue
                    stack.append(nei)

            return 1

        count = 0
        for u in graph:
            count += dfs(u)

        return count
