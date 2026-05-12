from collections import deque
from typing import Optional
from problems.binary_trees.tree_node import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root

    def invertTreeBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

    def invertTreeDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        stack = [root]

        while stack:
            node = stack.pop()

            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root