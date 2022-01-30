"""
---
number:67
title:Add Binary
difficulty:easy
tags:
- addition
- binary
- xor
---
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""


class Solution:
    def cheeky(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary(self, A: str, B: str) -> str:
        longest = A if len(A) > len(B) else B
        shortest = A if longest == B else B

        carry = 0
        result = []

        for i, b in enumerate(reversed(longest)):
            b = int(b)
            index = len(shortest) - i - 1

            if index < 0:
                result.append(str(carry ^ b))
                if carry + b > 1:
                    carry = 1
                else:
                    carry = 0
            else:
                a = int(shortest[index])
                result.append(str(a ^ b ^ carry))

                if a + b + carry > 1:
                    carry = 1
                else:
                    carry = 0

        if carry:
            result.append(str(carry))

        return "".join(reversed(result))


def test_1():
    assert Solution().addBinary("11", "1") == "100"
