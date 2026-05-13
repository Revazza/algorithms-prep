from typing import Optional

from problems.binary_trees.tree_node import TreeNode


class Codec:

    def __init__(self):
        self.root_index = 0

    def serialize(self, root: Optional[TreeNode]) -> str:

        values = []

        def serializeDFS(node: TreeNode):
            if not node:
                values.append("N")
                return

            values.append(str(node.val))
            serializeDFS(node.left)
            serializeDFS(node.right)

        serializeDFS(root)

        return ",".join(values) # 1,2,3,N,N,4

    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.root_index = 0

        def deserializeDFS() -> TreeNode:
            if values[self.root_index] == "N":
                self.root_index += 1
                return None

            root = TreeNode(int(values[self.root_index]))
            self.root_index += 1
            root.left = deserializeDFS()
            root.right = deserializeDFS()

            return root
        
        return deserializeDFS()
