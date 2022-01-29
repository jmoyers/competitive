"""
---
title: Letter Combinations of a Phone Number
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/letter-combinations-of-a-phone-number
---
Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.

I'm not putting the picture here. 2 = abc, 7 = pqrs, 9 = wxyz these are the
only non-obvious ones

Note:

Although the above answer is in lexicographical order, your answer could be
in any order you want.
"""
from typing import List, Dict


class Solution:
    letters: Dict[str, List[str]] = {
        "1": [],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def dfs(self, digits: str, index: int, path: List[str], result: List[str]) -> None:
        if len(path) == len(digits):
            result.append("".join(path))
            return

        for letter in self.letters[digits[index]]:
            self.dfs(digits, index + 1, path + [letter], result)

    def letterCombinations(self, digits: str) -> List[str]:
        """
        This looks like a classic backtracking problem, where the permutations
        being explored have a problem space defined by the set of letters
        associated with each number.
        """
        if len(digits) == 0:
            return []

        result: List[str] = []

        self.dfs(digits, 0, [], result)

        return result


def test_1():
    result = Solution().letterCombinations("23")
    assert result == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


def test_2():
    result = Solution().letterCombinations("")
    assert result == []
