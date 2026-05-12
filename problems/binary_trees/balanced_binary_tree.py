from typing import Optional

from problems.binary_trees.tree_node import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        is_balanced, height = self.balance(root)

        return is_balanced

    def balance(self, root: TreeNode) -> tuple[bool, int]:
        if not root:
            return True, 0

        left_balanced, left_height = self.balance(root.left)
        right_balanced, right_height = self.balance(root.right)

        return (left_balanced and right_balanced and abs(right_height - left_height) <= 1,
                1 + max(left_height, right_height))