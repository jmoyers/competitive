"""
---
title: Reverse Integer
difficulty: easy
level: 1
tags:
- integer
- reverse
- overflow
- modulus
links: 
- https://leetcode.com/problems/reverse-integer
---
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231, 231 − 1]. For the purpose of
this problem, assume that your function returns 0 when the reversed integer
overflows.
"""


class Solution:
    def reverse(self, x: int) -> int:
        str_int = str(x)
        ans = 0

        if str_int[0] == "-":
            ans = -int(str_int[:0:-1])
        else:
            ans = int(str_int[::-1])

        if -(2 ** 31) < ans < (2 ** 31) - 1:
            return ans
        return 0


result = Solution().reverse(123)
print(result)
assert result == 321

result = Solution().reverse(-123)
print(result)
assert result == -321

result = Solution().reverse(1534236469)
print(result)
assert result == 0
# Input: 120
# Output: 21
