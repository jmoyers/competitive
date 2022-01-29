"""
---
number: 472
title: Concatenated Words
difficulty: hard
tags:
- backtracking
- trie
- permutations
links:
- https://leetcode.com/problems/concatenated-words/
---
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
"""
from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Solution:
    def _buildTrie(self, words: List[str]):
        curr = self.root = TrieNode()

        for word in words:
            for c in word:
                curr = curr.children[c]
            curr.is_word = True
            curr = self.root

    def _checkConcat(self, word):
        curr = self.root
        for i, c in enumerate(word):
            curr = curr.children[c]
            if curr.is_word:
                if i == len(word) - 1:
                    self.count += 1
                    return True
                if self._checkConcat(word[i + 1 :]):
                    self.count += 1
                    return True
            if not curr.children:
                return False
        return False

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        buckets = defaultdict(list)
        min_bucket = float("inf")
        results = []

        self._buildTrie(words)

        for word in words:
            buckets[len(word)].append(word)

        for k in buckets.keys():
            min_bucket = min(k, min_bucket)

        for k, words in buckets.items():
            if k >= min_bucket * 2:
                for word in words:
                    self.count = 0
                    if self._checkConcat(word):
                        if self.count > 1:
                            results.append(word)

        return results


def test_lc1():
    inp = [
        "cat",
        "cats",
        "catsdogcats",
        "dog",
        "dogcatsdog",
        "hippopotamuses",
        "rat",
        "ratcatdogcat",
    ]
    out = ["catsdogcats", "dogcatsdog", "ratcatdogcat"]

    result = Solution().findAllConcatenatedWordsInADict(inp)
    assert set(result) == set(out)


def test_lc2():
    inp = ["cat", "dog", "catdog"]
    out = ["catdog"]

    result = Solution().findAllConcatenatedWordsInADict(inp)
    assert result == out
