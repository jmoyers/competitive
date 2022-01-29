"""
---
title: Reverse Nodes in k-Group
difficulty: hard
level: 3
tags:
- linked list
- reverse
- in-place
links: 
- https://leetcode.com/problems/reverse-nodes-in-k-group
---
Given a linked list, reverse the nodes of a linked list k at a time and
return its modified list.

k is a positive integer and is less than or equal to the length of the linked
list. If the number of nodes is not a multiple of k then left-out nodes in
the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, only nodes itself may be
    changed.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        val = self.val
        next = self.next.__str__() if self.next else None
        return f"{val} -> {next}"


class Solution:
    """
    Initial reaction is you use the same method as reversing a linked list in place, but
    keep track of a variable that denotes how many nodes you've reversed in this sequence.

    When you hit k nodes in this sequence, you start over. You also need to keep track
    of where the start of the current k-sequence is, so that when the current sequence
    is over, you can link the sequences together.

    You generall need 3 variables to reverse a list in place,
        1. prev node
        2. curr node
        3. next node

    Your goal is to take curr and point it at prev, then advance curr to next

    next -> curr -> prev

    i dont think there is anything that won't work with the standard


    Steps:
        save start
        loop for range(k) or end:
            store previous so we can point curr to it
            save currs next for next iter
            make curr point to previous
            advance curr to saved next

    """

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev: Optional[ListNode] = None
        curr: Optional[ListNode] = head
        next: Optional[ListNode] = None

        # start of this k-group
        start: Optional[ListNode] = None
        # end of last k-group
        end: Optional[ListNode] = None

        """
        1 -> 2 -> 3 -> 4
        s    c    n
        p

        k = 0

        if n:
            c.next = p
            c = n
            n = c.next if c else none

        k = 1

        s.next = c
        s = c
        c = c.next

        2 -> 1 -> 3 -> 4

        """

        while curr:
            count = 0

            # check if k nodes exist
            save = curr
            while count <= k - 1 and curr:
                curr = curr.next
                count += 1

            # we leave the trailing partial k-group alone
            if count != k:
                break

            curr = save
            count = 0

            # increment one node forward at the start of a group
            # and set the start node so that we can later point
            # the start to the next k-group
            start = curr
            prev = curr
            curr = curr.next
            next = curr.next if curr else None

            # only iterate reverse k - 1 nodes
            while count < k - 1 and curr:
                # grab the old node in front of current so that we can
                # progress to the next node after reverse is done
                next = curr.next

                # point the current node backward
                curr.next = prev

                # prepare for next iteration in two parts
                # for the next potential iteration move prev forward
                prev = curr

                # go to the next node
                curr = next
                count += 1

            # for the very first k-group we need to update the head to
            # point at the new start
            if head == start:
                head = prev

            # at the end of a k-group, point the "start" node, which is
            # actually the new end node for the group, to the start
            # of the next k-group, which should be the curr node
            start.next = curr

            # now we point the end of the last k-group to the new start
            # of the current k-group, which should be in prev
            if end:
                end.next = prev

            # store the end of this k-group, which was the old start of
            # it before reverse
            end = start

        return head


def test_reverse_1():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol = Solution().reverseKGroup(head, 3)
    print(sol)
    # hard to test, i punt


# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
