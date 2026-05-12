from typing import Optional, List

from problems.linked_list.list_node import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        nodes = {}

        for node in lists:
            head = node;
            while head:
                if head.val in nodes:
                    nodes[head.val] += 1
                else:
                    nodes[head.val] = 1;
                head = head.next;

        min = -1000;
        max = 1000;

        node = ListNode();
        tail = node;

        while min <= max:
            if min not in nodes:
                min += 1
                continue;

            count = nodes[min];
            while count != 0:
                temp = ListNode(min);
                tail.next = temp;
                tail = tail.next;
                count -= 1

            min += 1

        return node.next;
