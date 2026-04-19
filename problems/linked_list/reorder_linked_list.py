import math
from typing import Optional

from problems.linked_list.list_node import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        nodes = []

        temp = head

        while temp:
            nodes.append(temp)
            temp = temp.next

        left = 0
        right = len(nodes) - 1

        while left < right:
            nodes[left].next = nodes[right]
            left += 1

            if left == right:
                break

            nodes[right].next = nodes[left]
            right -=1

        nodes[left].next = None

        return None
