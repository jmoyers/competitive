"""
---
title: Maximal Rectangle
difficulty: hard
level: 3
tags:
- histogram
- dynamic programming
- matrix
- find maximum
links: 
- https://leetcode.com/problems/maximal-rectangle
---
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
containing only 1's and return its area.


"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        # for each point keep track of
        # 1. left bound - iter left to right
        # 2. right bound - iter right to left
        # 3. height - add 1 for each '1' encountered, reset height on '0'

        # we'll reuse the same 1-dimensional lists for left, right, height
        # for height, each row will build on heights from previous rows
        # for width, the left and right bound will be the minimal width
        # for a given rectangle created by the height of the current column

        # we find the minimal width by max() left and min() right

        rows = len(matrix)
        cols = len(matrix[0])

        height = [0] * cols
        left = [0] * cols
        right = [cols] * cols

        area = 0

        for row in range(rows):

            curr_left, curr_right = 0, cols

            for col in range(cols):
                if matrix[row][col] == "1":
                    height[col] += 1
                else:
                    height[col] = 0

            for col in range(cols):
                if matrix[row][col] == "1":
                    left[col] = max(left[col], curr_left)
                else:
                    left[col] = 0
                    curr_left = col + 1

            for col in range(cols - 1, -1, -1):
                if matrix[row][col] == "1":
                    right[col] = min(right[col], curr_right)
                else:
                    right[col] = cols
                    curr_right = col

            for col in range(cols):
                area = max(area, height[col] * (right[col] - left[col]))

        return area


# result = Solution().maximalRectangle([
#    ["1","0","1","0","0"],
#    ["1","0","1","1","1"],
#    ["1","1","1","1","1"],
#    ["1","0","0","1","0"]
# ])
# print(result)
# assert(result == 6)

result = Solution().maximalRectangle(
    [
        ["1", "0", "1", "1", "0", "1"],
        ["1", "1", "1", "1", "1", "1"],
        ["0", "1", "1", "0", "1", "1"],
        ["1", "1", "1", "0", "1", "0"],
        ["0", "1", "1", "1", "1", "1"],
        ["1", "1", "0", "1", "1", "1"],
    ]
)

print(result)
assert result == 8
