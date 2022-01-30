"""
---
number: 131
title: Palindrome Partitioning
difficulty: medium
tags:
- palindrome
- recursion
- memoization
- backtracking
links:
- https://leetcode.com/problems/palindrome-partitioning/
---
Given a string s, partition s such that every substring of the partition is a
palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

from typing import List

class Solution:
    """
    can be nicely modeled as recursion
    find all permutations all partions
    check if each parition is a palindrome
    we'll be rechecking the same strings potentially
    our palindrome function can use a memo table to store results for
    later o 1 lookup
    """
    def __init__(self):
        self.pal_memo = {}
        self.memo = {}
        
    def is_pal(self, s):
        if len(s) == 1:
            return True
        
        if s in self.pal_memo:
            return self.pal_memo[s]
        
        rev = "".join(reversed(s))
        result = rev == s
        
        self.pal_memo[rev] = result
        self.pal_memo[s] = result
        
        return result
    
    def _partition(self, s: str, results):
        if len(s) == 1:
            results.append([s])
            return
        
        if s in self.memo:
            results.extend(self.memo[s])
            return
        
        if self.is_pal(s):
            results.append([s])
        
        for n in range(1, len(s)):
            left = s[:n]
            right = s[n:]
            if self.is_pal(left):
                result = []
                self._partition(right, result)
                if result:
                    for r in result:
                        results.append([left] + r)
        
        self.memo[s] = results
        
    def partition(self, s: str) -> List[List[str]]:
        results = []
        self._partition(s, results)
        return results
    
                    
        
