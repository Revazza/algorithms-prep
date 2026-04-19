from typing import Optional

from problems.linked_list.list_node import ListNode


class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:

        newHead = ListNode(0)
        tempHead = newHead

        while head1 and head2:

            if head1.val <= head2.val:
                newHead.next = head1
                head1 = head1.next
            else:
                newHead.next = head2
                head2 = head2.next

            newHead = newHead.next

        while head1:
            newHead.next = head1
            head1 = head1.next
            newHead = newHead.next

        while head2:
            newHead.next = head2
            head2 = head2.next
            newHead = newHead.next

        return tempHead.next
