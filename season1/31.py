"""
---
title: Next Permutation
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/next-permutation
---
Implement next permutation, which rearranges numbers into the
lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest
possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its
corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        The naive solution is to find all permutations, find where your
        current nums list is in the permutation list and take the next
        item.

        Unfortunately, this is n! time at a minmum, as finding all
        permutaitons is a backtracking problem which can be expressed as a
        tree exploring a decreasing problem space.

        So, we need to identify some other property of increasing/decreasing
        permutation patterns. One helpful way to analyze a given permutation
        is to look from the end of the string and find the first
        non-decreasing number.

        For instance:
            4 3 8 7 6 5 2 1
              ^
        
        In this sequence, 3 is the first non-decreasing number. If you
        carefully analyze a decision tree baesd on a sorted list of integers,
        you'll note that the last permutation in the set is always a
        decreasing list. You can work this out to be true by intuition due to
        how the next branch is selected (temporally). So with this
        observation, you can come to the conclusion that the first
        non-decreasing number in the suffix is a point of interest (the pivot
        for this branch exploration)

        Because we've identified the pivot, we can then swap it with the next
        logical choice for branch exploration. In this case its 5, because 4
        has already been removed from the problem space because its already
        been placed in slot 1.

        So we have:
            4 5 8 7 6 3 2 1
              ^       ^

        However, because this was the LAST permutation in the 3 rooted
        problem space associated with that branch, we have one more operation
        left. We need to adjust the rest of the list such that its the FIRST
        permutation to explore for the 5 rooted branch. The first permutation
        is always going to be an increasing sort due to the nature of
        permutation selection (you select the first available input in the
        sorted initial list). So, if we reverse array slice for the range
        after the pivot, we should have the first permutation of the 5 rooted
        branch.

        So then we have (answer):
            4 5 1 2 3 6 7 8
                < ------- >
                 reversed
        """

        # identify the pivot
        pivot: int = 0

        for i in reversed(range(len(nums))):
            if i + 1 < len(nums) and nums[i] < nums[i + 1]:
                pivot = i
                break

        # slice out the already-rooted prefix and find the next logical
        # number for branch exploration, which should be the next largest
        # number in the partition
        part_length = len(nums) - (pivot + 1)
        to_swap = -1

        for i in reversed(range(pivot + 1, part_length + pivot + 1)):
            if nums[pivot] < nums[i]:
                to_swap = i
                break

        if to_swap != -1:
            nums[pivot], nums[to_swap] = nums[to_swap], nums[pivot]

            # finally we can reverse the right parition to get the first parition
            # rather than the last partition
            nums[pivot + 1 :] = nums[:pivot:-1]
        else:
            # if we found no swap candidate, this is the last permutation
            # rooted at this pivot, so we'd need to either back up one branch,
            # or if this is the first index, purely reverse the range
            nums.reverse()


def test_1():
    input = [1, 2, 3]
    Solution().nextPermutation(input)
    print(input)
    assert input == [1, 3, 2]


def test_2():
    input = [4, 3, 8, 7, 6, 5, 2, 1]
    Solution().nextPermutation(input)
    print(input)
    assert input == [4, 5, 1, 2, 3, 6, 7, 8]


def test_3():
    input = [3, 2, 1]
    Solution().nextPermutation(input)
    print(input)
    assert input == [1, 2, 3]


test_3()
