from typing import Optional

from problems.linked_list.list_node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        newHead = ListNode(0)

        while head is not None:
            temp_next = head.next
            temp = newHead.next
            newHead.next = head
            newHead.next.next = temp
            head = temp_next

        return newHead.next
