from typing import Optional

from problems.binary_trees.tree_node import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = [(root, 1)]
        max_level = 1

        while stack:
            (node, level) = stack.pop()

            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
            max_level = max(level, max_level)

        return max_level