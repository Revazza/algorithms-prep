from typing import List, Optional

from problems.binary_trees.tree_node import TreeNode


class Solution:

    def __init__(self):
        self.root_index = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_set = {val: idx for idx, val in enumerate(inorder)}

        def build(left: int, right: int) -> TreeNode:
            if left > right:
                return None

            root = TreeNode(preorder[self.root_index])
            self.root_index += 1
            mid = inorder_set[root.val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root


        return build(0, len(preorder) - 1)
