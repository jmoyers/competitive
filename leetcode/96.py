"""
---
number: 96
title: Unique Binary Search Trees
difficulty: medium
tags:
- binary search tree
- recursion
- dynamic programming
- permutations
- partitioning
links:
- https://leetcode.com/problems/unique-binary-search-trees/
---
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:

1 <= n <= 19
"""
from itertools import permutations


class Solution:
    """
    I initially though that this might be a strict permutation problem where
    we looked at the total permutations for a given list of integers. Then
    I realized that, its not all permutations, because to satisfy the condition
    of BST, we have to disallow some from existing (we can't have a number
    larger than the root anywhere on the left of the tree). So then I thought of
    paritioning the tree into left and right subtrees. Then I thought of the
    fact that if there were 2 combinations on the left and two combinations on
    the right of the tree, there'd actually be 4 permutations (2*2). Then I
    realized even the subtrees have to follow the same invariant, so it occured
    to me that this is modeled well by recursion. Because its a perfect
    subproblem split, I thought we could likely use memoization, since the list
    on both sides of the root parition both follow the same structure. After
    that, I looked at the answer to make sure I wasn't way off base. I was not,
    so we moved forward with the recursive solution using partitioning or
    pivoting by root.

    As I thought at the very beginning, it turns out that this can also be
    computed strictly by math -- this is the catalan sequence which appears in
    combinatorics quite a bit, but there is no chance I'm memorizing that. Could
    be mentioned in an interview and discuss that this is a n**2 implementation,
    by catalan (because each number in the seq depends on prev number) it could
    be reduced to an O(n) implementation with a reference text to help compute
    the number.
    """

    def __init__(self):
        self.memo = {}

    def numTrees(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        if 0 <= n <= 1:
            return 1
        elif n == 2:
            return 2

        count = 0

        for i in range(1, n + 1):
            count += self.numTrees(i - 1) * self.numTrees(n - i)

        self.memo[n] = count

        return count


def test_1():
    assert Solution().numTrees(3) == 5


def test_2():
    assert Solution().numTrees(4) == 14
