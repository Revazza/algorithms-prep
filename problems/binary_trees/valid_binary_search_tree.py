from collections import deque
from typing import Optional

from problems.binary_trees.tree_node import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        queue = deque([(root, -1001, 1001)])

        while queue:
            (node, min_value, max_value) = queue.popleft()

            if not node.val > min_value or not node.val < max_value:
                return False

            if node.left:
                queue.append((node.left, min_value, node.val))

            if node.right:
                queue.append((node.right, node.val, max_value))

        return True
