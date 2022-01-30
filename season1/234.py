"""
---
number:234
title:Palindrome Linked List
difficulty: easy
tags:
- linked list
- reverse
- palindrome
---
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spacePalindrome(self, head: ListNode) -> bool:
        curr = head
        running = 0

        while curr:
            running ^= curr.val
            curr = curr.next

        return running == 0

    def isPalindrome(self, head: ListNode) -> bool:
        store = []

        curr = head

        while curr:
            store.append(curr.val)
            curr = curr.next

        return store == list(reversed(store))


def test_lc1():
    l = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    assert Solution().isPalindrome(l)
    assert Solution().spacePalindrome(l)


def test_lc2():
    l = ListNode(0, ListNode(2, ListNode(2, ListNode(1))))
    assert Solution().isPalindrome(l) == False
    assert Solution().spacePalindrome(l) == False
