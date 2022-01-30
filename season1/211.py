"""
---
number:211
title: Add and Search Word - Data structure design
difficulty: medium
tags:
- trie
- backtracking
- recursion
- hash map
- permutations
links:
- https://leetcode.com/problems/add-and-search-word-data-structure-design/
---
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""


"""
Base data structure: hash map
- Since the regex is limited to . replacement, we don't need to do any backtracking or branch management for search
- Do all the work of the dot replacement up front
- dictionary -> keys are
    - "word"
    - all permutations of "word" such that one to len(word) are replaced
        - "word", ".ord", "..rd", "...d", "....", ".o.rd", ...
        - each permutation is a key set to value = true
- trie approach
    - imagine two words such that "word" "bord" -> ".ord"
        - inside the trie you have to take both child branches all way down
        - assuming one branch doesn't work out -- or say the first 5 branches doesn't work out, you have to backtrack to where you made a decision based on . replacement and take the other branches to their dfs conclusion one at a time.
"""

"""
Trie approach
"""
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        if len(word) == 0:
            return

        curr = self.root

        for c in word:
            curr = curr.children[c]

        curr.word = True

    def search(self, word: str) -> bool:
        return self._dfs(word, self.root)

    def _dfs(self, word: str, curr) -> bool:
        if word == "":
            return curr.word

        if word[0] == ".":
            # iterate all children in the dot case
            for child in curr.children.values():
                if self._dfs(word[1:], child):
                    return True
        else:
            if word[0] not in curr.children:
                return False

            if self._dfs(word[1:], curr.children[word[0]]):
                return True


"""
Precomputed hash map approach - slow to build words, fast to search
"""


class WordDictionaryMap:
    def __init__(self):
        self.store = {}

    def _perms(self, word, path, results):
        if word == "":
            results.append("".join(path))
            return
        self._perms(word[1:], path + ["."], results)
        self._perms(word[1:], path + [word[0]], results)

    def addWord(self, word: str) -> None:
        # generate permutations for word such that each
        # letter is replaced with . in every possible position
        results = []
        self._perms(word, [], results)
        # use each permutation as a dictionary key
        for key in results:
            self.store[key] = True

    def search(self, word: str) -> bool:
        return word in self.store


def test_lc1():
    w = WordDictionary()
    w.addWord("bad")
    w.addWord("dad")
    w.addWord("mad")
    assert w.search("pad") == False
    assert w.search("bad") == True
    assert w.search(".ad") == True
    assert w.search("b..") == True


def test_lc2():
    w = WordDictionary()
    w.addWord("ran")
    w.addWord("rune")
    w.addWord("runner")
    w.addWord("runs")

    assert w.search("r.n")
    # ["addWord","addWord","addWord","addWord","addWord","addWord","addWord","addWord","search","search","search","search","search","search","search","search","search","search"]
    # [["ran"],["rune"],["runner"],["runs"],["add"],["adds"],["adder"],["addee"],["r.n"],["ru.n.e"],["add"],["add."],["adde."],[".an."],["...s"],["....e."],["......."],["..n.r"]]
