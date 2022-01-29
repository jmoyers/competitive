"""
---
number:93
title:Restore IP Addresses
difficulty:medium
tags:
- backtracking
- recursion
- ip address
- parsing
- pruning
links:
- https://leetcode.com/problems/restore-ip-addresses/
---

1291

505

Add to List

Share
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""
from typing import List


class Solution:
    def _count(self, path):
        count = 0
        for p in path:
            count += len(p)
        return count

    def _restore(self, s, path, results):
        # no leading zeroes
        if path and len(path[-1]) > 1 and path[-1][0] == "0":
            path.pop()
            return

        # too few characters even at max
        if path and self._count(path) + (4 - len(path)) * 3 < len(self.s):
            path.pop()
            return

        # too many characters even at min
        if path and self._count(path) + (4 - len(path)) * 1 > len(self.s):
            path.pop()
            return

        # fragment not between 0 -> 255
        if path and int(path[-1]) > 255:
            path.pop()
            return

        if s == "":
            results.append(".".join(path))
            return

        for i in range(min(3, len(s))):
            self._restore(s[i + 1 :], path + [s[: i + 1]], results)

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []

        self.s = s
        results = []
        self._restore(s, [], results)
        return results


def test_lc1():
    inp = "25525511135"
    results = Solution().restoreIpAddresses(inp)
    assert results == ["255.255.11.135", "255.255.111.35"]


def test_lc2():
    inp = "010010"
    results = Solution().restoreIpAddresses(inp)
    assert results == ["0.10.0.10", "0.100.1.0"]
