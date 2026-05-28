from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = dict()
        for i in range(len(edges)):
            graph[i + 1] = []

        def has_cycle(start):

            visited = set()
            stack = [(start, -1)]

            while stack:
                node, parent = stack.pop()

                if node in visited:
                    continue

                visited.add(node)

                for nei in graph[node]:

                    if nei == parent:
                        continue

                    if nei in visited:
                        return True

                    stack.append((nei, node))

            return False

        for u, v in edges:

            graph[u].append(v)
            graph[v].append(u)

            if has_cycle(u):
                return [u, v]

        return []
