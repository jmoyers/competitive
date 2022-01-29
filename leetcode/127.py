"""
---
title: Word Ladder
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/word-ladder
---
Given two words (beginWord and endWord), and a dictionary's word list, find
the length of shortest transformation sequence from beginWord to endWord,
such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.
"""
from typing import List, Set, Dict, Deque, Tuple
from collections import deque


class Solution:
    """
    Seems like a backtracking-style problem, but with a focus on finding the
    shortest path, rather than all paths.

    Because its a shortest path algorithm, we can express it as a breadth-first
    search, so it will likely be iterative instead of recursive. We should use
    a queue.

    The possible choices are the overlap of all one letter changes to the current
    word and the words available in the dictionary.

    If you calculate this intersection, you have defined the problem space at
    each stage. You'd have to recalculate this every iteration, so special
    attention should be paid to make this cheap.

        Maybe naive?
            1. Iterate over both current word and candidate word, calculating
                total character count difference. One index.
            2. Once character count difference grows larger than 1, abandon
            3. You are left with a List[str] of potential branches from this node
            4. Once you calculate this adjacency list, it doesn't need to be
                recalculated because we will enforce 1 visit with a visited set.
        
        Maybe less naive?
            1. Use the current word as a base and calculate its "generic" forms.
            2. Generic forms: Hot -> *ot, H*t, Ho*
            3. I'm not convinced this is any better, as you still need to character
                compares left to right and you still need to do the compare to
                every other word.
    
    My above take times out. It seems there is an optimization you can make due to
    the nature of the problem. You can calculate the path from both sides due to
    how node adjacency works with this issue. Because a graph search like this gets
    much, much larger at each level, an extremely large word list can produce an
    enormous graph. This can get out of hand for both time and memory.

    You can "cut the problem in half" by starting a search from both sides. If
    you ever find a node that is in the visited list from the other search, you
    can terminate your search and add the depths together to get the lenth
    of the search path.
    """

    def __init__(self):
        self.word_list: Set[str]

    def visitWord(
        self,
        queue: Deque[Tuple[str, int]],
        end: str,
        visited: Dict[str, int],
        other: Dict[str, int],
    ) -> int:

        word, depth = queue.popleft()

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwyxz":
                w = word[:i] + c + word[i + 1 :]

                if w in self.word_list:
                    if w in other:
                        return other[w] + depth
                    if w in self.word_list and w not in visited:
                        visited[w] = depth + 1
                        queue.append((w, depth + 1))

        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        self.word_list = set(wordList)
        top_queue: Deque[Tuple[str, int]] = deque()
        bottom_queue: Deque[Tuple[str, int]] = deque()

        # we need to keep the depth at every visited word, because if one
        # traversal encounters a world from the other, we need to add their
        # depths together _at that point_ to get the path length
        top_visited: Dict[str, int] = {beginWord: 1}
        bottom_visited: Dict[str, int] = {endWord: 1}

        top_queue.append((beginWord, 1))
        bottom_queue.append((endWord, 1))

        while top_queue and bottom_queue:
            path = self.visitWord(top_queue, endWord, top_visited, bottom_visited)

            if path > 0:
                return path

            path = self.visitWord(bottom_queue, beginWord, bottom_visited, top_visited)

            if path > 0:
                return path

        return 0


def test_1():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    assert Solution().ladderLength(beginWord, endWord, wordList) == 5


def test_2():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    # hit -> hot -> dot -> dog -> cog

    assert Solution().ladderLength(beginWord, endWord, wordList) == 0


def test_3():
    beginWord = "lost"
    endWord = "cost"
    wordList = ["most", "fist", "lost", "cost", "fish"]

    assert Solution().ladderLength(beginWord, endWord, wordList) == 2
    # cost -> most
    #  1       2
    # lost -> most
    #  1       2


def test_4():
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"]

    assert Solution().ladderLength(beginWord, endWord, wordList) == 3
    # what it should catch
    # hot -> dot
    # dog -> dot

    # what is catches
    # hot -> hog -> cog
    # dog -> cog


def test_5():
    beginWord = "lost"
    endWord = "miss"
    wordList = ["most", "mist", "miss", "lost", "fist", "fish"]

    assert Solution().ladderLength(beginWord, endWord, wordList) == 4
    # lost ->
    # miss


def test_6():
    beginWord = "ymain"
    endWord = "oecij"
    wordList = [
        "ymann",
        "yycrj",
        "oecij",
        "ymcnj",
        "yzcrj",
        "yycij",
        "xecij",
        "yecij",
        "ymanj",
        "yzcnj",
        "ymain",
    ]

    assert Solution().ladderLength(beginWord, endWord, wordList) == 10


def test_7():
    beginWord = "sail"
    endWord = "ruip"
    wordList = [
        "rain",
        "ruin",
        "gain",
        "ruip",
        "grin",
        "grit",
        "sail",
        "main",
        "pain",
        "pair",
        "pail",
        "mail",
    ]
    assert Solution().ladderLength(beginWord, endWord, wordList) == 6
