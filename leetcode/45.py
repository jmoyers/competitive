"""
---
number: 45
title: Jump Game II
difficulty: hard
tags:
- greedy
- dynamic programming
- memoization
- intervals
links:
- https://www.youtube.com/watch?v=zwh2sjdDzBM
- https://leetcode.com/problems/jump-game-ii
---
"""
from typing import List

from typing import List


class Solution:
    """
    Spent an hour working on a backtracking solution, but the problem with
    a backtracking solution is that for each index, you have to iterate over
    ALL the indexes from 0 -> value at that index. This can mean say 25000 
    iterations for a single index. And memoization doesn't necessarily help
    prune that tree enough.

    It turns out because we have a contiguous monotonically increasing set
    of spots we can land (just the indexes of the array), there is a greedy
    algorithm.
    """

    def jump(self, nums: List[int]):
        N = len(nums)

        if N <= 1:
            return 0

        # we linearly step through the array with current
        current = 0

        # current_max is the maximum number of jumps that we find in the next
        # sequence. so if we look at say 2, 3, 1
        #                                ^
        # we examine 2, which says: look at the next two numbers, find which is
        # larger. the larger number, as long as its not past the end of our
        # array, is the best jump possible
        #
        # i think it really comes down to there is no reason to not choose the
        # largest number, because it can represent any possible jump from that
        # index to any index up to n in front of it. so if at each possible
        # window, we always choose the largest number, we'll always minimize the
        # number of jumps

        next_max = current_max = nums[current]
        jump = 1

        while current_max < N - 1:
            # for each index, examine the sequence to find the largest next
            # possible jump. if you do this throughout
            while current <= current_max:
                next_max = max(next_max, current + nums[current])
                current += 1
            current_max = next_max
            jump += 1

        return jump

    """
    Here be my bad dp solution that dies because each number at given index
    can be a very large number, and so therefore represent a huge number of
    invalid branches
    """

    def __init__(self):
        self.memo = {}

    def _jump(self, nums: List[int], index, jumps) -> int:
        if index == len(nums) - 1:
            return jumps

        key = index

        if key in self.memo:
            return self.memo[key] + jumps

        min_jumps = float("inf")

        curr = nums[index]

        end = min(curr + 1 + index, len(nums))

        for i in reversed(range(index + 1, end)):
            min_jumps = min(min_jumps, self._jump(nums, i, jumps + 1))

        self.memo[key] = min_jumps - jumps
        return min_jumps

    def bad_dp_sol(self, nums: List[int]) -> int:
        return self._jump(nums, 0, 0)


def test_1():
    inp = [2, 3, 1, 1, 4]
    assert Solution().jump(inp) == 2


def test_2():
    nums = [1, 2, 1, 1, 1]
    assert Solution().jump(nums) == 3
