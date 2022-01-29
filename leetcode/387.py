"""
---
number: 387
title: First Unique Character in a String
difficulty: easy
tags:
- frequency counter
- hash map
- filter
- ordered hash map
---

Given a string, find the first non-repeating character in it and return its
index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

Note: You may assume the string contains only lowercase English letters.
"""
from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = OrderedDict()

        for i, c in enumerate(s):
            if c not in chars:
                chars[c] = [i, 1]
            else:
                chars[c][1] += 1

        for c, rec in chars.items():
            index, count = rec[0], rec[1]
            if count < 2:
                return index
        return -1
