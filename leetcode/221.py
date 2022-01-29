"""
---
title: Maximal Square
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/maximal-square
---
Given a 2D binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
from typing import List


class Solution:
    """
    The fact that its a square is important. You could use the more complex
    alogorithm for finding the maximal rectangle and it works here. However,
    it might be that there's a smaller, easier to grok solution here.

    Rectangle:
        * Examine each row
            * Find the height of a given histogram bar by comparing it to
                the results from the last row. You don't need to store this
                in a matrix, it can be a simple list, cause we are going
                to collapse the needed information into one row (dp sol)
            * Find information on the right and left bound by iterating from
                the right (reverse iter) and left. This is a dp sol as well,
                we use the min of the right and the max of the left to find
                the minimum width required
        * Due to it being a square, we then need to take the min of the width
            and height and thats the area we consider for new max area
    """

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        max_area = 0

        height = [0] * len(matrix[0])
        left = [0] * len(matrix[0])
        right = [len(matrix[0])] * len(matrix[0])

        for i in range(len(matrix)):

            # as we iterate thru the columns we need to keep track of the
            # last seen edge. so if we encounter a 0, we are a minimum at
            # j + 1 for the left-most edge up to this point
            curr_left, curr_right = 0, len(matrix[0])

            # height
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0

            # left
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    # we compare the left edge for this row to the left edges
                    # we've seen so far amongst all the rows to get the
                    # minimal left edge in the column
                    left[j] = max(left[j], curr_left)
                else:
                    left[j] = 0
                    curr_left = j + 1

            # right
            for j in reversed(range(len(matrix[0]))):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], curr_right)
                else:
                    right[j] = len(matrix[0])

                    # because we're reverse iterating and this is 0 indexed
                    # this is just equal to j here
                    curr_right = j

            # max area for each column
            for j in range(len(matrix[0])):
                w = right[j] - left[j]
                h = height[j]

                square_side = min(w, h)

                max_area = max(max_area, square_side ** 2)

        return max_area

    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        """
        Just a description, not going to implement it.

        This will be faster than the more general algorithm above and is 
        somewhat harder to understand.

        1. If you notice that a square with side length of size 3 is made up
        of 4 overlapping squares of side length 2, you can use this
        observation to "build up" an answer. 
        
        2. First, you need to have a place to represent the identity of a given square. If you are iterating left to right, top to bottom, it makes sense that the bottom right cell in a square would be the last thing you'd look at, so we can use this cell to identify the square.

        3. So, if you iterate through each index and examine the "next
        largest" square for that cell, which is a square of side length two,
        you'll be looking at 3 additional cells besides yourself. Above you,
        to the left of you, and diagonally up and left. If those cells all
        also contain 1s, you have a square with side length 2. So, you store
        a 2 in the memoized matrix at the index of that bottom right cell.

        4. Now, the next step is to understand how to translate that value of
        2 into something useful in the process of "building up" the answer
        for the next cells we encounter that could be a part of that
        already-identified square. If you consider that each cell is itself a
        square of size 1, you can put a base value of 1 in all the squares
        that contain a 1 on the input matrix. With that pre-condition,
        consider the following way of figuring out what the value is in a
        given square in the memo matrix: 
            min(memo[r][c - 1], memo[r - 1][c - 1], memo[r - 1][c]) + 1

        So, if we have:
            1  1
            1  2
               ^ this value is 2 because min(1,1,1) + 1 = 2
        
        5. The key is that as the square expands, the fact that a square of +
        1 size is made up of 4 overlapping squares of - 1 size. This will
        lead the value in the cell to "build-up" from the 4 previous squares
        and increment the side length appropriately for that cell
        representing the larger square. Just have to noodle on this for a
        minute to see it.
        """
        pass


def test_1():
    result = Solution().maximalSquare(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )

    assert result == 4
