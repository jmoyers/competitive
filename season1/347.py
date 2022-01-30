"""
---
number: 347
title: Top K Frequent Elements
difficulty: medium
tags:
- top k
- array
- integer
- frequency counter
- heap
---

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.

    Your algorithm's time complexity must be better than O(n log n), where n
    is the array's size.

    It's guaranteed that the answer is unique, in other words the set of the
    top k frequent elements is unique.

    You can return the answer in any order.
"""

from typing import List
from collections import Counter


class Solution:
    """
    If we count up frequency of int with a dict, then get a list of the
    items in the dict and sort it, we should be able to slice the first k
    items off the array.
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = sorted(list(Counter(nums).items()), key=lambda i: -i[1])
        return [n for (n, f) in freq[:k]]


def test_lc1():
    nums, k = [1, 1, 1, 2, 2, 3], 2
    assert Solution().topKFrequent(nums, k) == [1, 2]


def test_lc2():
    input, k = [4, 1, -1, 2, -1, 2, 3], 2
    assert Solution().topKFrequent(input, k) == [-1, 2]

