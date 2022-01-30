"""
---
title: Decode Ways
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/decode-ways
---
A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number
of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: "226"
Output: 3
Explanation:
It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""
from typing import ByteString, List


class Solution:
    """
    This looks like a backtracking problem.

    Problem space is defined by taking 1 or 2 digits from the front of
    the string.

    This can be expressed as a recursive function with:
        s - input string, prefix of 1 and 2 characters inrementally
            removed to form branches form problem space
        
        return
            int - the number of successful branches produced by string
    
    It appears there is a faster and more concise pure tabular dp solution
    that is harder to understand. It basically revolved around computing
    the number of branches for index i, and then relating it to the
    number of branches from i - 1 and i - 2. dp[0] = 1 is sort of the 
    base case that says that a one character string has 1 successful branch.
    
    Then from there you update the index twice, one for the one character
    branch and once for the 2 character branch if they are valid input.
    Still have to check for "0" as the 1 character branch and disregard.

    Similar problems:
        62. Unique Paths
        70. Climbing Stairs
        509. Fibonacci Number
    
    I still have problems groking pure tabular solutions without carefully
    stepping through the code.
    """

    def __init__(self):
        self.cache = {}

    def numDecodings(self, s: str) -> int:
        return self.helper(s)

    def helper(self, s) -> int:
        if s in self.cache:
            return self.cache[s]

        valid_branches = 0

        p1 = len(s) >= 1 and 1 <= int(s[0]) <= 9
        p2 = p1 and len(s) >= 2 and 1 <= int(s[0:2]) <= 26

        if p1:
            suffix_count = self.helper(s[1:])

            if len(s) == 1:
                valid_branches += 1
            elif suffix_count > 0:
                valid_branches += suffix_count

        if p2:
            suffix_count = self.helper(s[2:])
            if len(s) == 2:
                valid_branches += 1
            elif suffix_count > 0:
                valid_branches += suffix_count

        self.cache[s] = valid_branches
        return valid_branches


def test_1():
    input = "12"
    output = 2
    assert Solution().numDecodings(input) == output


def test_2():
    input = "226"
    output = 3
    assert Solution().numDecodings(input) == output


# It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
def test_3():
    input = "0"
    output = 0
    assert Solution().numDecodings(input) == output


def test_4():
    input = "01"
    output = 0
    assert Solution().numDecodings(input) == output
