"""
---
title: Longest Consecutive Sequence
difficulty: hard
level: 3
tags:
- number sequence
- set
links: 
- https://leetcode.com/problems/longest-consecutive-sequence
---
Given an unsorted array of integers, find the length of the longest
consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.
"""
from typing import List, Dict, Set, Union


class Solution:
    """
    My initial solution was to use a dictionary to store the streak so far, build
    up the dictionary over time by looking at the previous item, as well as to
    update all items that exist in the number list going forward. So in that way
    as we encounter a each number, even if out of order dp[n] would always have
    the largest streak once we've iterated through everything.

    However, this is still n * average sequence size, because you may need to
    update the dp sequence internally over and over if you encounter the numbers 
    in reverse order seperated from each other.

    So, a different construction is to first construct a set from the numbers
    for O(1) lookup time. Then iterate through the set, but only start searching
    for a sequence length once you've reached the start of a list (n - 1 is not
    in the set). This guarantees that you'll only ever iterate over a number
    once because we only initiate the sequence count from the start of a sequence.
    This is because it is the definition of the start of a sequence if n - 1 does
    not exist!
    """

    def longestConsecutive(self, nums: Union[Set[int], List[int]]) -> int:
        if not nums:
            return 0

        nums = set(nums)

        max_sequence_length = 0

        for n in nums:
            if n - 1 not in nums:
                sequence_length = 1

                while n + 1 in nums:
                    sequence_length += 1
                    n += 1

                max_sequence_length = max(max_sequence_length, sequence_length)

        return max_sequence_length


def test_1():
    input = [100, 4, 200, 1, 3, 2]
    assert Solution().longestConsecutive(input) == 4

