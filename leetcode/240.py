"""
---
number: 240
title: Search a 2D Matrix II
difficulty: medium
tags:
- binary search
- brain bender
---
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Two ways make intuitive sense to me.
        1. search each row with binary search - nlogn. seems to leave something
            on the table because we are not using the fact the other dimension
            is sorted
        2. if you realize that if you can isolate one dimension for each of the
            two choices (left/right, up/down) you can get an n + m solution.
            you have to go to the highest side in one dimension and the lowest
            side in the other dimension. in this way, if you find that the 
            target is lower/higher than your current element, you only have one
            choice. you have to noodle on this for a second to understand why
            that is the case. in this way we examine at most n + m elements, 
            which is quite fast.
        """

        # start at the bottom left corner. this maximizes the value found in the
        # row and minimizes the value found across the columns.
        if not matrix or not matrix[0]:
            return False

        r, c = len(matrix) - 1, 0

        while r >= 0 and c < len(matrix[0]):
            el = matrix[r][c]

            if el == target:
                return True
            elif el < target:
                c += 1
            else:
                r -= 1

        return False


def test_lc1():
    inp = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]

    assert Solution().searchMatrix(inp, 4)
    assert Solution().searchMatrix(inp, 19)
    assert Solution().searchMatrix(inp, 24)
    assert Solution().searchMatrix(inp, 14)
    assert Solution().searchMatrix(inp, 100) == False
