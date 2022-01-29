"""
---
number: 136
title: Single Number
difficulty: easy
tags:
- bit manipulation
- xor
- frequency counter
- hash map
links:
- https://leetcode.com/problems/single-number/
---
Given a non-empty array of integers, every element appears twice except for
one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)

        for n, c in counts.items():
            if c == 1:
                return n

    def xorSolution(self, nums: List[int]) -> int:
        """
        Neat! 0 xor number = number, number xor number = 0, n1 ^ n2 ^ n1 = (n1 ^
        n1) ^ n2 = 0 ^ n2 = n2
        """
        result = 0

        for n in nums:
            result ^= n

        return result

