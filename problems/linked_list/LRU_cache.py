from collections import defaultdict


class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node()
        self.nodes = {}
        self.right = Node()
        self.capacity = capacity

        self.left.next = self.right
        self.right.prev = self.left
        pass

    def remove(self, key: int):
        node = self.nodes[key]

        prev = node.prev
        node.next.prev = prev
        prev.next = node.next

        del self.nodes[key];

    def insert(self, key:int, value: int):

        node = Node(key, value)

        prev = self.right.prev

        self.right.prev = node
        node.next = self.right

        prev.next = node
        node.prev = prev

        self.nodes[key] = node

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.remove(key)
        self.insert(key, node.val)

        return self.nodes[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.nodes:
            self.insert(key, value)
        else:
            self.remove(key)
            self.insert(key, value)

        if len(self.nodes) > self.capacity:
            lru = self.left.next
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
            del self.nodes[lru.key]



