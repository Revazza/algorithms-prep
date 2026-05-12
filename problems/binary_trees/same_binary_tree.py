from typing import Optional

from problems.binary_trees.tree_node import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if p and not q:
            return False
        if q and not p:
            return False

        if q.val != p.val:
            return False

        is_left_same = self.isSameTree(p.left, q.left)
        is_right_same = self.isSameTree(p.right, q.right)

        return is_left_same and is_right_same
