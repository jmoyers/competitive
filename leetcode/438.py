"""
---
title: Find All Anagrams in a String
number: 438
difficulty: medium
tags:
- anagram
- counter
- frequency
- hash map
links:
- https://leetcode.com/problems/find-all-anagrams-in-a-string/
---
Given a string s and a non-empty string p, find all the start indices of p's
anagrams in s.

Strings consists of lowercase English letters only and the length of both
strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
from typing import List
from collections import Counter
from copy import copy


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        results = []
        counts = Counter(p)

        if len(p) > len(s):
            return []

        # set up our counter such that its valid for 0 -> len(p)
        for i in range(len(p)):
            if s[i] in counts:
                counts[s[i]] -= 1

        if all(v == 0 for v in counts.values()):
            results.append(0)

        for i in range(1, len(s) - len(p) + 1):
            if i > 0 and s[i - 1] in counts:
                counts[s[i - 1]] += 1

            if s[i + len(p) - 1] in counts:
                counts[s[i + len(p) - 1]] -= 1
                if all(v == 0 for v in counts.values()):
                    results.append(i)

        return results


def test_lc1():
    s = "abab"
    p = "ab"
    result = Solution().findAnagrams(s, p)
    assert result == [0, 1, 2]

