from typing import Optional

from problems.linked_list.list_node import ListNode
from problems.linked_list.node import Node


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> 'Optional[Node]':

        created = {}

        newHead = Node(0)
        tempHead = newHead

        while head:
            newNode = Node(head.val)

            if head in created:
                newNode = created[head]
            else:
                created[head] = newNode

            if head.random and head.random in created:
                newNode.random = created[head.random]
            else:
                if head.random:
                    newNode.random = Node(head.random.val)
                    created[head.random] = newNode.random

            tempHead.next = newNode
            tempHead = tempHead.next
            head = head.next

        return newHead.next