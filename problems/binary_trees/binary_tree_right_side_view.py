from collections import deque
from typing import Optional, List

from problems.binary_trees.tree_node import TreeNode

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        visible = []

        queue = deque([(root, 0)])

        while queue:
            (root, level) = queue[-1]
            visible.append(root.val)

            while queue and queue[0][1] == level:
                (node, _) = queue.popleft()

                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

        return visible
