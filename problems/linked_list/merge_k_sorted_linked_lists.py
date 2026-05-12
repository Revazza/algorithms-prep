from typing import Optional, List

from problems.linked_list.list_node import ListNode


class Solution:
    def mergeKLists(self, lists):
        return self.divide(0, len(lists) - 1, lists)

    def divide(self, start, end, lists):
        if start > end:
            return None

        if start == end:
            return lists[start]

        mid = (start + end) // 2

        left = self.divide(start, mid, lists)
        right = self.divide(mid + 1, end, lists)

        return self.merge(left, right)

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        if left:
            tail.next = left

        if right:
            tail.next = right

        return dummy.next