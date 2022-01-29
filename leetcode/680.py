"""
---
title: Valid Palindrome II
difficulty: easy
level: 1
tags:
- string
- parsing
- reverse
- branching
- backtracking
links: 
- https://leetcode.com/problems/valid-palindrome-ii
---
Given a non-empty string s, you may delete at most one character. Judge
whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True

Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:

    The string will only contain lowercase characters a-z. The maximum length
    of the string is 50000.
"""


class Solution:
    """
    Checking a palindrome is usually reversing a string and checking if its
    equal. If you language can use a generator for this, it shouldn't take
    any extra time to use a reverse() type method, which I think python can.

    If we find a bad character, there are two cases for which we need to be 
    aware. The first is that the character on the right partition is the
    bad character. The second is the character on the left half of the
    partition is the bad one. We need to check both cases. Because we're
    only allowing 1 bad character, this means the algorith still runs in
    2n which is linear.
    """

    def validPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                # i-1:j+1 is valid
                # so we either remove i or remove j
                # if neither works its invalid
                o1 = s[:i] + s[i + 1 :]
                o2 = s[:j] + s[j + 1 :]

                return o1 == o1[::-1] or o2 == o2[::-1]

        return True


def test_1():
    input = "aba"
    assert Solution().validPalindrome(input)


def test_2():
    input = "abca"
    assert Solution().validPalindrome(input)


def test_3():
    input = "abbbcbba"
    assert Solution().validPalindrome(input)
