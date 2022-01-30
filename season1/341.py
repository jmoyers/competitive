"""
---
number: 341
title: Flatten Nested List Iterator
difficulty: medium
tags:
- iterator
- stack
- reverse
links:
- https://leetcode.com/problems/flatten-nested-list-iterator/
---
NOTE: don't have all the code to run this -- they did not provide implmentation
of NestedInteger

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be
integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
"""


class NestedIterator:
    def __init__(self, nestedList):
        self.stack = []

        def dfs(l, r):
            if isinstance(l, list):
                for i in l[::-1]:
                    dfs(i, r)
            elif l.isInteger():
                r.append(l.getInteger())
            else:
                dfs(l.getList(), r)

        dfs(nestedList, self.stack)

    def next(self):
        return self.stack.pop()

    def hasNext(self):
        return len(self.stack) > 0

