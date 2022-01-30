"""
---
title: Special Binary String
difficulty: hard
level: 3
tags:
- parition
- string
- frequency
- dictionary
- hash map
links: 
- https://leetcode.com/problems/special-binary-string
---
A string S of lowercase English letters is given. We want to partition this
string into as many parts as possible so that each letter appears in at most
one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
splits S into less parts.

Note:

    S will have length in range [1, 500].
    S WILL CONSIST OF LOWERCASE ENGLISH LETTERS ('A' TO 'Z') ONLY.
"""

from typing import List
from collections import defaultdict


class Solution:
    """
    We can calculate index ranges for each letter.
    With the index ranges, at a minimum, we have to find the overlapping
    parition ranges. That should literally be the answer.

    Initally each character starts as its own parition. Overlap ov
    Go through each character range. Find all overlapping ranges. Add to one
    parition. The partition range grows.

    """

    def partitionLabels(self, s: str) -> List[int]:
        ranges = defaultdict(lambda: [len(s), -1])

        for i, c in enumerate(s):
            ranges[c][0] = min(ranges[c][0], i)
            ranges[c][1] = max(ranges[c][1], i)

        partitions = []

        for c in ranges.keys():
            found = False
            for i, p in enumerate(partitions):
                if p[0] <= ranges[c][0] <= p[1]:
                    found = True
                    p[1] = max(p[1], ranges[c][1])
            if not found:
                partitions.append(ranges[c])

        return [(end - start) + 1 for start, end in partitions]


def test_1():
    input = "ababcbacadefegdehijhklij"
    output = [9, 7, 8]
    assert set(Solution().partitionLabels(input)) == set(output)
    # The partition is "ababcbaca", "defegde", "hijhklij".
