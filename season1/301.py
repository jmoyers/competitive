"""
---
title: Remove Invalid Parentheses
difficulty: hard
level: 3
tags:
- string
- parsing
- permutation
- backtracking
- set
- shortest path
links: 
- https://leetcode.com/problems/remove-invalid-parentheses
---
Remove the minimum number of invalid parentheses in order to make the input
string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()() ()", "( ())()"]

Example 2:

Input: "(a)())()"
Output: ["(a)() ()", "(a ())()"]

Example 3:

Input: ")("
Output: [""]
"""
from typing import List
from itertools import permutations


class Solution:
    """
    This is a permutation problem because of "all possible results"

    This is a backtracking problem.

    You can jump through many hoops to try to prune the possible candidates
    to remove. The naive solution seems to be O(2**n), because there are 2
    choices (keep and remove) for each character. You cannot assume that only
    parens which aren't matched are part of the valid paths list, becuase of
    cases like:

    "())(((()m)("
    "()   (()m) "
    solutions = ["()(()m)"]

    In this solution, you'll notice that both opens and closes are removed,
    not just 'dangling' close parens.
    
    This means that every character needs to be examined for keep/discard
    choice, and every permutation needs to be checked for validity in the
    'naive' solution.
    
    You can definitely remove trailing opens and prefix closes, they are
    strictly invalid. e.g. ")("
    """

    def removeInvalidParentheses(self, s: str) -> List[str]:
        def valid(s: str):
            nO, nC = 0, 0
            for c in s:
                if c == "(":
                    nO += 1
                if c == ")":
                    nC += 1
                    if nC > nO:
                        return False

            return nC == nO

        # remove postfix opens
        i, to_remove = len(s) - 1, []

        # because of cases like )d)) we can't have nice things
        while i >= 0 and (s[i] == "(" or s[i] not in ("(", ")")):
            if s[i] == "(":
                to_remove.append(i)
            i -= 1

        if to_remove:
            s = "".join([s[i] for i in range(len(s)) if i not in to_remove])

        # remove prefix closes
        i, to_remove = 0, []

        while i < len(s) and (s[i] == ")" or s[i] not in ("(", ")")):
            if s[i] == ")":
                to_remove.append(i)
            i += 1

        if to_remove:
            s = "".join([s[i] for i in range(len(s)) if i not in to_remove])

        # create a set that will store our closest-to-the-original results
        results = {s}

        # each iteration we check if the results are valid, and if they are
        # we'll return those results. if not we're create a new set that
        # contains a version of the string for which each index is removed
        # on the second iteration it will include all the results of the
        # previos iteration, and in this way, we will get progressively smaller
        # strings that are further from the original input string. so when we
        # finally do find the correct result it will be the smallest available
        # `checked` here creates a list of only the valid strings in the set

        # breadth first search, because we're checking all possible children
        # for each string length before moving down

        while True:
            # here we filter for validity
            checked = [r for r in results if valid(r)]

            if checked:
                return checked

            # we don't check for validity here, just progressively add all
            # permutations, valid or not, to the set (each iteration includes
            # strings which are one character shorter)
            results = {s[:i] + s[i + 1 :] for s in results for i in range(len(s))}

        return list(results)


def test_close():
    input = "()())()"
    out = set(["(())()", "()()()"])

    assert set(Solution().removeInvalidParentheses(input)) == out


def test_open():
    input = "((()(())("
    out = set(["((()))", "(()())", "()(())"])
    assert set(Solution().removeInvalidParentheses(input)) == out


def test_other_characters():
    input = "a"
    out = set(["a"])
    assert set(Solution().removeInvalidParentheses(input)) == out


def test_embedded_characters():
    input = "(a)())()"
    out = set(["(a)()()", "(a())()"])
    assert set(Solution().removeInvalidParentheses(input)) == out


def test_only_trailing():
    input = ")("
    out = [""]
    assert Solution().removeInvalidParentheses(input) == out


def test_lc1():
    input = "()(()(("
    out = set(["()()"])
    assert set(Solution().removeInvalidParentheses(input)) == out


def test_lc2():
    input = ")(()c))("
    out = set(["((c))", "(()c)"])
    assert set(Solution().removeInvalidParentheses(input)) == out


def test_lc3():
    input = "(((()(()"
    out = set(["()()", "(())"])
    assert set(Solution().removeInvalidParentheses(input)) == out


def test_lc4():
    input = "())(((()m)("
    # ( ) ) ( ( ( ( ) m ) (
    # ( )       ( ( ) m )
    out = ["()(()m)"]
    assert Solution().removeInvalidParentheses(input) == out

