from typing import Optional

from problems.binary_trees.tree_node import TreeNode


class Solution:
    maxDiameter:int = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter(root);
        return self.maxDiameter

    def diameter(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = self.diameter(root.left)
        right = self.diameter(root.right)
        self.maxDiameter = max(left + right, self.maxDiameter)

        return 1 + max(left, right)
