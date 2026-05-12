from problems.binary_trees.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, first: TreeNode, second: TreeNode) -> TreeNode:
        current = root

        while current:
            if current.val < first.val and current.val < second.val:
                current = current.right
            if current.val > first.val and current.val > second.val:
                current = current.left
            else:
                return current

        return current