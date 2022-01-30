"""
---
title: Kth Largest Element in an Array
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/kth-largest-element-in-an-array
---
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
from typing import List
from heapq import heappush, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        My intuition says that you can just use a min heap of size k
        to find the kth largest element.

        Since we don't have the whole list to heapify, building the
        heap should take O(n * log k) where k is the height of the heap
        we are enforcing
        """

        heap: List[int] = []

        for n in nums:
            heappush(heap, n)

            if len(heap) > k:
                heappop(heap)

        return heap[0]


def test_1():
    result = Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
    assert result == 5


def test_2():
    result = Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    assert result == 4
