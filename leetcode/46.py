"""
---
title: Permutations
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/permutations
---
Given a collection of distinct integers, return all possible permutations.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        self.dfs(nums, [], result)
        return result

    def dfs(self, nums: List[int], path: List[int], result: List[List[int]]) -> None:
        """
        Use backtracking to create a list of all permutation for numbers in
        the given array.

            Parameters
                nums - the list of numbers from which to permute. we take a
                number from this list each time we wish to explore that
                branch

                path - the numbers, in-order, taken from the nums array so
                far. these represent a partial solution as well as the
                decision tree explored in this branch

                result - a passed by reference solution only updated once
                we've completely explored the decision space represented by
                nums. so we only fill this array once nums is empty. other
                branches will update this same array, so this is a list of
                lists
        """

        # base case, this means we've completely explored the problem space
        if not nums:
            result.append(path)

        # to explore every possible branch from this point, we loop through
        # the possiblilities in the problem space, i.e. each option in nums
        for i in range(len(nums)):
            # fast copy list with new branch element to be removed
            reduced_problem_space = nums[:i] + nums[i + 1 :]

            self.dfs(reduced_problem_space, path + [nums[i]], result)


def test_1():
    result = Solution().permute([1, 2, 3])
    assert result == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


test_1()
