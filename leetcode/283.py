"""
---
title: Move Zeroes
number: 283
difficulty: easy
tags:
- dual pointer
links:
- https://leetcode.com/problems/move-zeroes/
---
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # will always be a pointer to the first 0, so that when we swap it
        # with a non-zero number, it will be at the end of the list of known
        # non-zeros
        zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1


def test_lc1():
    inp = [0, 1, 0, 3, 12, 0]
    out = [1, 3, 12, 0, 0, 0]

    Solution().moveZeroes(inp)

    assert inp == out
