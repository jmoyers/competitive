"""
---
title: Find All Duplicates in an Array
difficulty: medium
tags:
- in place
- sorting
- duplicates
- integers
links:
- https://leetcode.com/problems/find-all-duplicates-in-an-array/
---
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
from typing import List


class Solution:
    """
    Use the sign of the value stored at n - 1 to indicate whether we've seen a
    value. Goofy answer. In reality, you would just use a much smaller data type
    for the array and make a hash map if you valued your sanity at all.
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        results = []
        for i in range(len(nums)):
            v = abs(nums[i])
            if nums[v - 1] < 0:
                results.append(v)
            nums[v - 1] *= -1
        return results


def test_lc1():
    inp = [4, 3, 2, 7, 8, 2, 3, 1]
    out = [2, 3]

    result = Solution().findDuplicates(inp)
    assert result == out
