"""
---
number:9
title:Palindrome Number
difficulty:easy
tags:
- palindrome
- integer
- modulus
- math
links:
- https://leetcode.com/problems/palindrome-number/
---
Determine whether an integer is a palindrome. An integer is a palindrome when
it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it
becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits = []
        place = 10

        while x:
            mod = x % place
            digits.append(mod // (place // 10))
            place *= 10
            x = x - mod

        return digits == digits[::-1]

    def cheeky(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
