from typing import Optional
from wsgiref.util import request_uri

from problems.binary_trees.tree_node import TreeNode

class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        return self.findIsSame(root, sub_root)

    def isSame(self, root: TreeNode, sub_root: TreeNode) -> bool:
        if not root and not sub_root:
            return True

        if root and sub_root and root.val == sub_root.val:
            return self.isSame(root.left, sub_root.left) and self.isSame(root.right, sub_root.right)

        return False

    def findIsSame(self, root: TreeNode, sub_root: TreeNode) -> bool:
        if not root:
            return False

        if root.val == sub_root.val and self.isSame(root, sub_root):
            return True

        left = self.findIsSame(root.left, sub_root)
        right = self.findIsSame(root.right, sub_root)

        return left or right