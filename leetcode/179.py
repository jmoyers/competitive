"""
---
number: 179
title: Largest Number
difficulty: medium
tags:
- sorting
- string
- parsing
- custom sort
- maximum
links:
- https://leetcode.com/problems/largest-number/
---
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        So this appears to be something you can solve in O(N) time.
        
        Split the values by digit, create a tuple of digits.
        Sort the tuples by first digit, then subsequent digits. '9' > '94' > '85'
        We also need to make sure that the shortest largest digits are before longer tuples with more
        digits attached to them, though '9' and '99' have equivalent sort preference.
        
        95, 4, 93, 98, 7, 6
        """

        digits = []

        for n in nums:
            ns = list(str(n))
            digits.append(ns)

        def compare(a, b):
            # this is genius. i would have been hard pressed to think of this.
            # i had been trying to come up with some sort of custom sorting
            # algorithm that took into account length and then in addition to
            # length, using a direct comparison of indexes. while there is a
            # chance it would have worked, it was hopelessly complex and had
            # a ton of edge cases
            s1 = a + b
            s2 = b + a
            return -1 if s1 > s2 else 1

        digits = sorted(digits, key=cmp_to_key(compare))

        flattened = []

        for d in digits:
            for n in d:
                flattened.append(n)

        leading = -1

        for i, d in enumerate(flattened[: len(flattened) - 1]):
            if d != "0":
                break
            leading = i

        flattened = flattened[leading + 1 :]

        return "".join(flattened)


def test_1():
    inp = [3, 30, 34, 5, 9]
    assert Solution().largestNumber(inp) == "9534330"


def test_2():
    inp = [1, 1, 1]
    assert Solution().largestNumber(inp) == "111"


def test_3():
    inp = [999999998, 999999997, 999999999]
    out = "999999999999999998999999997"
    assert Solution().largestNumber(inp) == out


def test_4():
    inp = [0, 0]
    assert Solution().largestNumber(inp) == "0"


def test_5():
    inp = [824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247]
    assert Solution().largestNumber(inp) == "9609938824824769735703560743981399"


def test_6():
    inp = [121, 12]
    assert Solution().largestNumber(inp) == "12121"
