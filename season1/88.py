"""
---
title: Merge Sorted Array
difficulty: easy
level: 1
tags:
- sorting
- merging
- array
- in-place
- swap
links: 
- https://leetcode.com/problems/merge-sorted-array
---
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m and n
    respectively. You may assume that nums1 has enough space (size that is
    greater or equal to m + n) to hold additional elements from nums2.
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # my intuition says this is just like the inner function of a merge sort
        # where you keep two pointers, one for each list, pick the larger number
        # from either of the two lists and slot it into n1, shifting over as necessary

        # a slightly more non-obvious solution is to keep a copy of the first
        # m values in num1, and use that copy to do comparisons and never
        # slide any values over

        # a more obvious but requiring O(n + m) extra space is just to make
        # a new list and then copy that list over nums1 before returning

        # another way to is reverse iterate and use 3 points, one to the end
        # of num1, one to the end of nums2, and one to nums1[m].

        i1, i2 = 0, 0

        while i2 < len(nums2):
            if nums1[i1] < nums2[i2] and i1 < m:
                i1 += 1
            else:
                # shift everything in nums1 over
                temp = i1

                while temp < len(nums1):
                    nums1[temp], nums2[i2] = nums2[i2], nums1[temp]
                    temp += 1

                m += 1
                i2 += 1


def test_1():
    n1 = [1, 2, 3, 0, 0, 0]
    Solution().merge(n1, 3, [2, 5, 6], 3)
    assert n1 == [1, 2, 2, 3, 5, 6]
