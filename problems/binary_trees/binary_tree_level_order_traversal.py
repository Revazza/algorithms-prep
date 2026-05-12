from collections import deque
from typing import Optional, List

from problems.binary_trees.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        result = []
        queue = deque([(root, 0)])

        while queue:
            level = queue[0][1]
            values = []
            while queue and queue[0][1] == level:
                (node, _) = queue.popleft()
                values.append(node.val)
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

            result.append(values)

        return result
