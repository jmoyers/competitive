"""
---
title: Word Break II
difficulty: hard
level: 3
tags:
- string
- parsing
- trie
- dynamic programming
- prefix
- prefix table
- backtracking
- dfs
links: 
- https://leetcode.com/problems/word-break-ii
---
Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, add spaces in s to construct a sentence where each word is a
valid dictionary word. Return all such possible sentences.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.
"""
from typing import List, Iterable, Dict, Any


class Solution:
    def __init__(self):
        self.cache: Dict[str, List[str]] = {}

    def wordBreak(self, s: str, words: Iterable[str]) -> List[str]:
        """
        Approach 1:
            DFS/backtracking/permutation with a trie, which is just a tree of prefixes.
            We do a depth-first traversal where once we encounter a node indicating we've
            encountered a word, we subtract that word from the input string and start
            from the top of the trie.

            If we encounter a node with multiple children, this is an opportunity for back
            tracking, so once we iterate through all available branches to search for
            possible solutions.

        Approach 2:
            Dynamic programming (memo table) where we simply iterate through our dictionary
            checking for word prefixes on the current string.

            Subtract the word from the front of the input string. Recurse.

            Store the results of a traversal in a table, so if we encounter the same prefixes
            again we can simply pull from the table instead of reparsing the string.
        
        We'll go with approach 2 as it seems simpler and more concise.
        """

        # we'll use a set to get O(1) lookup time
        words = set(words)

        result = self.helper(s, 0, words)

        return result

    def helper(self, s: str, start: int, words: Iterable[str]) -> Any:
        if s[start:] in self.cache:
            return self.cache[s[start:]]

        results = []

        for i in range(start + 1, len(s) + 1):
            if s[start:i] in words:
                if i < len(s):
                    splits = self.helper(s, i, words)

                    for split in splits:
                        results.append(s[start:i] + " " + split)
                # base case
                else:
                    results.append(s[start:i])

        self.cache[s[start:]] = results

        return results


def test_1():
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]

    result = Solution().wordBreak(s, wordDict)
    assert set(result) == set(["cats and dog", "cat sand dog"])


def test_onecharacter():
    s = "a"
    wordDict = ["a"]
    result = Solution().wordBreak(s, wordDict)
    assert set(result) == set(["a"])


def test_3():
    s = "aaaaaaa"
    wordDict = ["aaaa", "aaa"]
    result = Solution().wordBreak(s, wordDict)
    assert set(result) == set(["aaaa aaa", "aaa aaaa"])


#
# Example 2:
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
# Example 3:
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
