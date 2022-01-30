"""
---
title: Regular Expression Matching
difficulty: hard
level: 3
tags:
- regex
- kleene star
- parsing
- string
- backtracking
- queue
- iterative
links: 
- https://leetcode.com/problems/regular-expression-matching
---
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like . or *.

"""
from typing import Callable, List, Deque, Tuple, Any
from collections import deque


class MatchCharGreedy:
    def __init__(self, op: Callable):
        self.op = op

    def __call__(self, s: str, i: int) -> List[int]:
        start = i

        while self.op(s, i) == i - 1 and i >= 0:
            i -= 1

        # short-circuit empty strings
        if s == "":
            i -= 1

        # backtracking options
        return list(range(start, i - 1, -1))

    def __str__(self):
        return f"{self.op}*"


class MatchChar:
    def __init__(self, c: str):
        self.c = c

    def __call__(self, s: str, i: int) -> int:
        if len(s) > i >= 0 and s[i] == self.c:
            return i - 1
        else:
            return -2

    def __str__(self):
        return self.c


class MatchAny:
    def __call__(self, s: str, i: int) -> int:
        if i < len(s):
            return i - 1
        else:
            return -2

    def __str__(self):
        return "."


def classify(p: str, i) -> Tuple[int, Callable]:
    if p[i] == "*" and i - 1 >= 0 and p[i - 1] != "*":
        # gobble 2, allow the greedy char to be .
        i, next_op = classify(p, i - 1)
        return (i, MatchCharGreedy(next_op))
    elif p[i] == "*":
        # need a character preceding *
        raise Exception()
    elif p[i] == ".":
        return (i - 1, MatchAny())
    else:
        return (i - 1, MatchChar(p[i]))


class Solution:
    def debugBranch(self, s, branch):
        print(s)
        print("".join(str(op) for op in list(branch)[::-1]))
        print()

    def isMatch(self, s: str, p: str) -> bool:
        if p == "" and s == "":
            return True

        queue: Deque[Callable] = deque()

        # build function queue
        i: Any = len(p) - 1

        while i >= 0:
            try:
                i, next_op = classify(p, i)
            except:
                return False

            queue.append(next_op)

        i = max(0, len(s) - 1)

        branches = [(i, queue.copy())]

        while branches and i != -1:
            i, branch = branches.pop()

            while branch:
                next_func = branch.popleft()

                i = next_func(s, i)

                # this last operation had branches
                if isinstance(i, list):
                    # short circuit for greedy matches on empty strings
                    if -1 in i and len(branch) == 0:
                        return True

                    for branch_index in i[1:]:
                        branches.append((branch_index, branch.copy()))
                    i = i[0]

                if i == -2:
                    break

            if len(branch) == 0 and i == -1:
                break
            else:
                i = -2

        return i == -1


def test_match1():
    result = Solution().isMatch("", ".ac*")
    assert result == False


def test_match2():
    result = Solution().isMatch("", "")
    assert result == True


def test_match3():
    result = Solution().isMatch("aaa", "ab*a")
    assert result == False


def test_match4():
    result = Solution().isMatch("", ".")
    assert result == False


def test_match5():
    result = Solution().isMatch("", ".*")
    assert result == True


def test_match6():
    result = Solution().isMatch("", "c*")
    assert result == True


def test_match7():
    result = Solution().isMatch("aa", "a")
    assert result == False


def test_match8():
    result = Solution().isMatch("aa", "a*")
    assert result == True


def test_match9():
    result = Solution().isMatch("aa", ".*")
    assert result == True


def test_match10():
    result = Solution().isMatch("ab", ".*")
    assert result == True


def test_match11():
    result = Solution().isMatch("aab", "c*a*b*")
    assert result == True


def test_match12():
    result = Solution().isMatch("mississippi", "mis*is*ip*.")
    assert result == True


def test_match13():
    result = Solution().isMatch("aaa", "ab*a*c*a")
    assert result == True
