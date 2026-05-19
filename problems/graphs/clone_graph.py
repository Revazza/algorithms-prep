from collections import deque
from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, start_node: Optional['Node']) -> Optional['Node']:
        if not start_node:
            return start_node

        queue = deque([start_node])
        clones = dict()
        clones[start_node] = Node(start_node.val)

        while queue:
            node = queue.popleft()
            clone = clones[node]

            for neighbor in node.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clone.neighbors.append(clones[neighbor])


        return clones[start_node]
