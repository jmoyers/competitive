"""
---
title: Two Sum
difficulty: easy
level: 1
tags:
- compliment
- dictionary
- hash map
links: 
- https://leetcode.com/problems/two-sum
---

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
"""


def twoSum(nums, target):
    # If we can quickly find if a compliment
    # exists in the data set, we've found the answer
    # If we loop through once, we can both check
    # for the compliment and create an O(1) lookup
    # map

    lookup = {}

    for i, num in enumerate(nums):
        compliment = target - num

        if compliment in lookup:
            return (i, lookup[compliment])

        lookup[num] = i

    return False


def test_1():
    result = twoSum([2, 7, 11, 15], 9)
    assert result == (1, 0)
