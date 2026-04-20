from typing import Optional

from problems.linked_list.list_node import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        size = 0
        tempHead = head
        while tempHead:
            size += 1
            tempHead = tempHead.next

        # [1,2,3,4, 5]
        # S = 5
        # n = 1

        tempHead = head
        prev = None
        count = 0
        while tempHead:

            if size - n == count:
                if prev is None:
                    return head.next
                temp = tempHead
                prev.next = temp.next
                temp.next = None
                break
            prev = tempHead
            tempHead = tempHead.next
            count += 1

        return head
