from typing import Optional, List

from problems.binary_trees.tree_node import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        result = []
        self.inorderTraversal(root, result, k)

        return result[k - 1]


    def inorderTraversal(self, node: TreeNode, result: List[int], k: int):
        if not node:
            return

        self.inorderTraversal(node.left, result, k)
        result.append(node.val)
        if len(result) == k:
            return
        self.inorderTraversal(node.right, result, k)

        return