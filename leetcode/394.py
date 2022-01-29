"""
---
title: Decode String
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/decode-string
---
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the
square brackets is being repeated exactly k times. Note that k is guaranteed
to be a positive integer.

You may assume that the input string is always valid; No extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any
digits and that digits are only for those repeat numbers, k. For example,
there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""


class Solution:
    """
    Stack models this nicely. Any time we encounter an encoded string,
    which can have nested encoded strings, we push the prev string onto
    the stack to save it, then the number (for which we're going to * by
    the result which we'll be calculating)

    We use a stack bc it can have nested expressions, so its the same
    concept as a parenthetical calculator.
    """

    def decodeString(self, s: str) -> str:
        # abc5[ab4[ab]]
        # abc
        # digit -> stash string, stash 5
        # if ] pop off stack, multiply string, pop orig string, append new
        # a b

        stack = []
        result = ""
        digits = []

        for c in s:
            # can be multiple digits
            if c.isdigit():
                digits.append(int(c))
            elif c == "]":
                multiple = stack.pop()
                inner = stack.pop()
                result = inner + (result * multiple)
            elif c == "[":
                n = 0
                place = 1

                while digits:
                    n += digits.pop() * place
                    place *= 10

                stack.append(result)
                stack.append(int(n))
                result = ""
            else:
                result += c

        return result


def test_1():
    s = "3[a]2[bc]"
    out = "aaabcbc"

    assert Solution().decodeString(s) == out


def test_2():
    s = "3[a2[c]]"
    out = "accaccacc"

    assert Solution().decodeString(s) == out


def test_3():
    s = "2[abc]3[cd]ef"
    out = "abcabccdcdcdef"

    assert Solution().decodeString(s) == out


def test_4():
    s = "abc3[cd]xyz"
    out = "abccdcdcdxyz"

    assert Solution().decodeString(s) == out


def test_5():
    s = "a100[a]"
    out = "a" + ("a" * 100)

    assert Solution().decodeString(s) == out
