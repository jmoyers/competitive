"""
---
number:148
title:Sort List
difficulty:medium
tags:
- linked list
- sort
- merge sort
links:
- https://leetcode.com/problems/sort-list/
---
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}->{self.next.__str__()}"


class Solution:
    def _mergeSort(self, head: ListNode) -> ListNode:
        if not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        first_half = self._mergeSort(head)
        second_half = self._mergeSort(second_half)

        return self._merge(first_half, second_half)

    def _merge(self, a: ListNode, b: ListNode):
        # create a dummy node and set next to the first item that is
        # placed on the newly created list
        dummy = ListNode()
        # keep a reference to current tail of the newly created list
        # as we go, so we can add new elements
        tail = dummy

        # loop until both a and b are empty
        while a or b:
            if a and b:
                if a.val < b.val:
                    tmp = a.next
                    a.next = None
                    tail.next = a
                    tail = tail.next
                    a = tmp
                else:
                    tmp = b.next
                    b.next = None
                    tail.next = b
                    tail = tail.next
                    b = tmp
            elif a:
                tail.next = a
                a = None
            else:
                tail.next = b
                b = None
        return dummy.next

    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        return self._mergeSort(head)


def test_1():
    l = ListNode(5, ListNode(4, ListNode(3, ListNode(1, ListNode(2, ListNode(-1))))))

    result = Solution().sortList(l)
    assert result.__str__() == "-1->1->2->3->4->5->None"
