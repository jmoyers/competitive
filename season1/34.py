"""
---
title: Find First and Last Position of Element in Sorted Array
number: 34
difficulty: medium
tags:
- binary search
links:
- https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
---
Given an array of integers nums sorted in ascending order, find the starting
and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9

"""
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect_left(nums, target)

        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        right = left

        while right < len(nums) and nums[right] == target:
            right += 1

        right -= 1

        return [left, right]

