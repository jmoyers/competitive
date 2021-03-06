"""
---
number: 126
title: Word Ladder II
difficulty: hard
---

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

from collections import deque
from typing import List


class Solution:
    def findLadders(
        self, begin_word: str, end_word: str, word_list: List[str]
    ) -> List[List[str]]:
        word_list = set(word_list)

        if end_word not in word_list:
            return []

        visited = {begin_word}

        queue = deque([[begin_word]])
        results = []
        depth = math.inf

        while queue:
            path = queue.popleft()
            word = path[-1]

            visited.add(word)

            if depth < len(path):
                break

            if word == end_word:
                results.append(path)
                depth = len(path)

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwyxz":
                    candidate = word[:i] + c + word[i + 1 :]
                    if candidate in word_list and candidate not in visited:
                        new_path = path + [candidate]
                        queue.append(new_path)

        return results
