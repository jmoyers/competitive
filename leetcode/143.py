"""
---
number: 143
title: Reorder List
difficulty: medium
tags:
- linked list
- interleaving
- stack
links:
- https://leetcode.com/problems/reorder-list/
---

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be
changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        curr = self
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        return " -> ".join(result)


class Solution:
    """
    My intuition was to modify without extra space per other linked list type
    problems, however, that means you have to iterate through the list
    count // 2 +/- 1 times. Thats a lot. So, decided to use a stack instead,
    simplifies the logic hugely, reduces runtime to n at the cost of O(n) space.
    """

    def reorderList(self, head: ListNode) -> None:
        if head is None:
            return None

        # the number of interleaves to do total based
        # on the count of the nodes
        reps = 0

        curr = head
        stack = []

        while curr:
            stack.append(curr)
            curr = curr.next

        # 1 -> 2 case needs no modification
        if len(stack) <= 2:
            return head

        curr = head
        reps = len(stack) // 2 - 1 if len(stack) % 2 == 0 else len(stack) // 2

        for _ in range(reps):
            stack[-2].next = None
            stack[-1].next = curr.next
            curr.next = stack[-1]
            curr = stack[-1].next
            stack.pop()


def test_even():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    Solution().reorderList(head)
    result = ListNode(1, ListNode(4, ListNode(2, ListNode(3))))
    assert head.__str__() == result.__str__()


def test_odd():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    Solution().reorderList(head)
    result = ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3)))))
    assert head.__str__() == result.__str__()
