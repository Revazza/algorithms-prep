import math
from typing import Optional

from problems.linked_list.list_node import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        reversedSecond = prev

        firstHead = head

        while reversedSecond:
            tempReversed = reversedSecond.next
            tempFirst = firstHead.next

            firstHead.next = reversedSecond
            reversedSecond.next = tempFirst

            firstHead = tempFirst
            reversedSecond = tempReversed

        return None
