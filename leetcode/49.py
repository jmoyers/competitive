"""
---
title: Group Anagrams
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/group-anagrams
---
Given an array of strings, group anagrams together.

Note:

    All inputs will be in lowercase.
    The order of your output does not matter.
"""
from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # in python there is a special type of set called a frozenset
        # which is immutable. it has a hash algorithm built-in, so we
        # can use it as a dictionary key

        # to determine whether something is an anagram we can use a
        # character frequency counter. from a freq counter dictionary
        # we can create a frozenset and use it as a key for a dictionary
        # of related anagrams (they have the same character frequency set)

        result = defaultdict(list)

        for s in strs:
            # built-in frequency counter. items returns a list of tuples,
            # so we'll get [(character: frequency) * n], which we can turn
            # into a set
            key = frozenset(Counter(s).items())

            # because we used a defaultdict we can just assume there is at
            # least an empty list at this key
            result[key].append(s)

        # should return a list of lists of strings grouped
        return [val for val in result.values()]


def test_1():
    results = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

    # easy compare, should not depend on order
    results = [set(r) for r in results]

    assert results == [set(["ate", "eat", "tea"]), set(["nat", "tan"]), set(["bat"])]
