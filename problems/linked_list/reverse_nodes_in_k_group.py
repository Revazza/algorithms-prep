from typing import Optional

from problems.linked_list.list_node import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev_tail = dummy

        while True:
            kth = self.getKth(prev_tail, k)
            if not kth:
                return dummy.next

            groupStart = prev_tail.next
            nextGroupStart = kth.next

            self.reverse(groupStart, nextGroupStart)

            prev_tail.next = kth

        return None

    def getKth(self, head:ListNode, k: int) -> ListNode:
        while head and k > 0:
            k -= 1
            head = head.next
        return head


    def reverse(self, left: ListNode, right: ListNode):
        prev = right.next
        current = left

        while current != right.next:
            temp_next = current.next
            current.next = prev
            prev = current
            current = temp_next