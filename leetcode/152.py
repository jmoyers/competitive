"""
---
number: 152
title: Maximum Product Subarray
difficulty: medium
---
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        """
        Not sure I can explain this one all that well. I'll try...

        result keeps track of the highest value we've ever seen

        max_product does not. conceptually its a little hard to follow or
        explain since it doesn't have a nice english sentence that makes
        intuitive sense of it. but basically it will always have either...
        1. n -- n itself is the highest number we've seen
        2. max_product * n -- pretty straightforward, multiply what we've seen
           so far by the new value we're encountering at n
        3. min_product * n -- this case where n is negative, min_product is
           negative and that results in a new highest positive number. note,
           that in the case where we get a chain of 3 negative numbers in a row,
           this does not result in an incorrect answer because of the way that
           min_product and max_product interact. at the second neg number, max
           product could get updated, but then in the same iteration, min
           product is set to n instead of n * min_product, because that yields
           a positive number.
        
        min_product in that way is the same, it will keep track of the most
        negative numbers we've seen. so in the case of 1 negative number, it
        gets updated, in the case of 2 negative numbers (which together form a
        positive number) it doesn't get updated, and then at 3 negative numbers
        is does get updated. so in this way, we make sure we keep track of
        negative number chains correctly, but its a bit hard to follow/grok.

        Also, zeroes are handled properly. if you hit a zero, the max(n*max,
        n*min, n) is always 0, so you reset both min and max and can continue on
        your way. 
        
        Pretty wild.
        """

        result = max_product = min_product = nums[0]

        for n in nums[1:]:
            temp = max(n * min_product, n * max_product, n)
            min_product = min(n * max_product, n * min_product, n)
            max_product = temp
            result = max(max_product, result)

        return result


def test_lc1():
    inp = [2, 3, -2, 4]
    assert Solution().maxProduct(inp) == 6


def test_lc2():
    inp = [-2, 0, -1]
    assert Solution().maxProduct(inp) == 0


def test_lc3():
    inp = [-2]
    assert Solution().maxProduct(inp) == -2


def test_lc4():
    inp = [-4, -3]
    assert Solution().maxProduct(inp) == 12


def test_lc5():
    inp = [2, -5, -2, -4, 3]
    assert Solution().maxProduct(inp) == 24
