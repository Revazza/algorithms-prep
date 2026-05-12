from problems.binary_trees.tree_node import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = [(root, root.val)]
        good_nodes = 0
        while stack:
            (node, path_max) = stack.pop()

            if node.val >= path_max:
                good_nodes += 1

            if node.left:
                stack.append((node.left, max(path_max, node.val)))
            if node.right:
                stack.append((node.right, max(path_max, node.val)))

        return good_nodes
