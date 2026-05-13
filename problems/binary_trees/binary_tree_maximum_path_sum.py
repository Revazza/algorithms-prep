import sys
from typing import Optional

from problems.binary_trees.tree_node import TreeNode


class Solution:
    def __init__(self):
        self.max_path = -sys.maxsize

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def calculate(node: TreeNode) -> int:
            if not node:
                return 0

            left_max = max(0, calculate(node.left))
            right_max = max(0, calculate(node.right))

            self.max_path = max(self.max_path, left_max + node.val + right_max)

            return node.val + max(left_max, right_max)

        calculate(root)

        return self.max_path
