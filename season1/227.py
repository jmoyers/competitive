"""
---
title: Basic Calculator II
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/basic-calculator-ii
---
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, /
operators and empty spaces . The integer division should truncate toward
zero.

Example 1:

Input: "3+2*2"
Output: 7

Example 2:

Input: " 3/2 "
Output: 1

Example 3:

Input: " 3+5 / 2 "
Output: 5

Note:

    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.
"""


class Solution:
    """
    Integer calculator. Doesn't talk about overflow.
    I assume it can have multiple digits per number.

    Operator precedence:
    - /, *
    - +, -

    Integer division is // in python.
    Need to parse the whole string and operate based on precedence.

    If it had parens, we'd want to use a stack, save results for a calculation
    when we find an open paren, pop them back off when we're done. No parens
    though.


    1 + 2 * 2 + 1
    --- ----- ---
     2    1    3

    2 * 2 = 4
    4 + 1 = 5
    5 + 1

    Tokenize
    1, +, 2, *, 2, +, 1

    Two precedence passes:
    1, +, 2, *, 2, +, 1
    1, +, 4, + 1 - pass 1
    6 - pass 2

    If you use a stack, this is a nice way to only loop once:

    def calculate(self, s):
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
        return sum(stack)
    """

    def calculate(self, s: str) -> int:
        # parse string, handle multiple digits
        tokens = []

        temp = []

        for c in s:
            if c.isdigit():
                temp.append(c)
            elif c in ("*", "/", "+", "-"):
                if len(temp) != 0:
                    # number waiting to be finished
                    tokens.append(int("".join(temp)))
                    temp.clear()
                tokens.append(c)

        if temp:
            tokens.append(int("".join(temp)))

        i = 0
        # multiplication, division pass
        while i < len(tokens):
            t = tokens[i]
            if t == "*":
                tokens[i - 1 : i + 2] = [tokens[i - 1] * tokens[i + 1]]
            elif t == "/":
                tokens[i - 1 : i + 2] = [tokens[i - 1] // tokens[i + 1]]
            else:
                i += 1

        i = 0
        # addition, subtraction pass
        while i < len(tokens):
            t = tokens[i]

            if t == "+":
                tokens[i - 1 : i + 2] = [tokens[i - 1] + tokens[i + 1]]
            elif t == "-":
                tokens[i - 1 : i + 2] = [tokens[i - 1] - tokens[i + 1]]
            else:
                i += 1

        return tokens[0]


def test_lc1():
    i = "3+2*2"
    o = 7

    assert Solution().calculate(i) == o


def test_lc2():
    i = " 3/2 "
    o = 1

    assert Solution().calculate(i) == o


def test_lc3():
    i = " 3+5 / 2 "
    o = 5

    assert Solution().calculate(i) == o


def test_lc4():
    i = "1+1+1"
    o = 3

    assert Solution().calculate(i) == o
