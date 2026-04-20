from typing import Optional

from problems.linked_list.list_node import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(0)
        tempHead = head
        carry = 0
        while l1 or l2:

            sum = carry

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry = sum // 10
            tempHead.next = ListNode(sum % 10)
            tempHead = tempHead.next

        if carry != 0:
            tempHead.next = ListNode(carry)

        return head.next