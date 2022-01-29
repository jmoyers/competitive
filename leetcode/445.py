"""
---
title: Add Two Numbers II
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/add-two-numbers-ii
---
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next


class Solution:
    """
    You need to at minimum know the length of the numbers so that
    in general we know the "place" of the digit in question.
 
    String method:
    Iterate thru both linked lists, appending to a string for each
    digit encountered. Covert to int at the end. Essentially the
    same as a stack based approach (we're doing the same thing).
    """

    def addTwoNumbers(self, l1: "ListNode", l2: "ListNode") -> "ListNode":
        n1, n2 = "0", "0"

        curr = l1
        while curr:
            n1 += str(curr.val)
            curr = curr.next

        curr = l2
        while curr:
            n2 += str(curr.val)
            curr = curr.next

        val = str(int(n1) + int(n2))

        dummy = ListNode()
        curr = dummy

        for c in val:
            curr.next = ListNode(int(c), None)
            curr = curr.next

        return dummy.next


def test_lc1():
    a = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
    b = ListNode(5, ListNode(6, ListNode(4)))
    out = ListNode(7, ListNode(8, ListNode(0, ListNode(7))))

    result = Solution().addTwoNumbers(a, b)

    curr = result
    verify = out
    while curr:
        assert curr.val == verify.val
        curr = curr.next
        verify = verify.next

