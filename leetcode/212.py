"""
---
number: 212
title: Word Search II
difficulty: hard
tags:
- trie
- graph
- dfs
links:
- https://leetcode.com/problems/word-search-ii/
---

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""

from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Solution:
    def __init__(self):
        self.visited = {}
        self.path = []
        self.result = set()

        # init in findWords
        self.board = None
        self.root = None

    def _build_trie(self, words: List[str]):
        self.root = TrieNode()
        curr = self.root
        for word in words:
            for c in word:
                curr = curr.children[c]
            curr.is_word = True
            curr = self.root

    def _dfs(self, r: int, c: int, curr: TrieNode):
        # visited
        if (r, c) in self.visited:
            return

        self.visited[(r, c)] = True

        character = self.board[r][c]

        self.path.append(character)

        curr = curr.children[character]

        # check if word
        if curr.is_word:
            self.result.add("".join(self.path))

        # check if trienode is a leaf and exit
        if not curr.children:
            del self.visited[(r, c)]
            self.path.pop()
            return

        # otherwise dfs
        # up
        if r >= 1:
            self._dfs(r - 1, c, curr)
        # down
        if r + 1 < len(self.board):
            self._dfs(r + 1, c, curr)
        # left
        if c >= 1:
            self._dfs(r, c - 1, curr)
        # right
        if c + 1 < len(self.board[0]):
            self._dfs(r, c + 1, curr)

        self.path.pop()
        del self.visited[(r, c)]

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []

        self.board = board
        self._build_trie(words)

        for r in range(len(board)):
            for c in range(len(board[0])):
                self._dfs(r, c, self.root)

        return list(self.result)


def test_1():
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]

    output = ["eat", "oath"]

    assert set(Solution().findWords(board, words)) == set(output)
