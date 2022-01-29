"""
---
number: 340
title: Longest Substring with At Most K Distinct Characters
difficulty: hard
tags:
- two pointer
- dual pointer
- frequency counter
- hash map
links:
- https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
---
Given a string, find the length of the longest substring T that contains at
most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
import math
from collections import defaultdict
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if s == "":
            return 0

        slow, fast, max_len = 0, 0, -math.inf

        counter = defaultdict(lambda: 0)

        while fast < len(s):
            counter[s[fast]] += 1

            while len(counter.keys()) > k:
                slow += 1
                counter[s[slow - 1]] -= 1
                if counter[s[slow - 1]] == 0:
                    del counter[s[slow - 1]]

            max_len = max(max_len, fast - slow + 1)
            fast += 1

        return max_len
