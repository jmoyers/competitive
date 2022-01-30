"""
---
number:300
title:Longest Increasing Subsequence
difficulty:medium
tags:
- dynamic programming
- binary search
- paitence sorting
- sorting
- longest subsequence
links:
- https://leetcode.com/problems/longest-increasing-subsequence/
- https://en.wikipedia.org/wiki/Patience_sorting
- https://www.youtube.com/watch?v=TocJOW6vx_I 
---

Given an unsorted array of integers, find the length of longest increasing
subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to
return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

from bisect import bisect_left
from typing import List


class Solution:
    # this is a tricky one to solve in n * logn time. it can be done
    # with binary search.

    # 1, 2, 5, 3, 4
    # https://www.youtube.com/watch?v=TocJOW6vx_I

    # 1. build a sequence from 0 -> the end of the array where each element
    #       is monotonically increasing
    # 2. when you encounter an element that is larger than the previous
    #       element in the array, find where it might belong in the sequence
    #       and replace the value that was there

    # steps...
    # 1
    # 1, 2
    # 1, 2, 5
    #
    # here we find that 3 would go after 2, and so we replace 5 with 3
    # 1, 2, 3
    # and so on

    # this finds the LENGTH of the subsequence, but not the subsequence
    # itself. this is so because if in the above example if you had a 0
    # at the very end of the input array (for example), you would place it
    # in the array at the very beginning. the 0 won't be in the actual
    # contiguous subsequence. my INTUITION about this is pretty bad, but i
    # feel that its a way of structurally filing away a number with the same
    # relationship to the data that its replacing. what i mean by this is
    # 0 in the above case is a 1 length subsequence (by itself), which
    # begins a new sequence.

    # its a form of https://en.wikipedia.org/wiki/Patience_sorting
    def lengthOfLIS(self, nums: List[int]) -> int:

        piles = []

        for n in nums:
            if not piles or piles[-1] < n:
                piles.append(n)
            else:
                i = bisect_left(piles, n)
                piles[i] = n

        return len(piles)


def test_lc1():
    inp = [10, 9, 2, 5, 3, 7, 101, 18]
    out = 4
    result = Solution().lengthOfLIS(inp)
    assert result == out


def test_lc2():
    inp = [10, 9, 2, 5, 3, 4]
    out = 3
    result = Solution().lengthOfLIS(inp)
    assert result == out


def test_lc3():
    inp = [2, 2]
    out = 1
    result = Solution().lengthOfLIS(inp)
    assert result == out
