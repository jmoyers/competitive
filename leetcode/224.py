"""
---
title: Basic Calculator
difficulty: hard
level: 3
tags:
- calculator
- stack
- parsing
- operator precedence
links: 
- https://leetcode.com/problems/basic-calculator
---
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus
+ or minus sign -, non-negative integers and empty spaces .

Note:

    You may asresulte that the given expression is always valid.
    Do not use the eval built-in library function.
"""
from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        # keep a running result
        result = 0

        # 1 if positive, -1 if negative
        sign = 1

        # multi-character number
        num = 0

        # if we encounter an open paren, we need to save the state
        # of the calculators running result and start fresh to calculate
        # whats inside the the parens. because they can be nested parens,
        # a stack can be used -- when you encounter a closing paren,
        # you simply grab the value off the top of the stack and add it
        # to the running result

        # in this way, subtraction can be handled properly, as it is not
        # associative (placement of parens matters)
        stack: List[int] = []

        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c in ["+", "-"]:
                result += sign * num
                sign = 1 if c == "+" else -1
                num = 0
            elif c == "(":
                # save the state of the calculator
                # you have to store the sign seperate from the result because
                # you can have something looking like this:
                #   2 - (5 - 3)
                #     ^
                # in this case, you don't want a negative 2 stored in the
                # result, as we're subtracting the result of whats enclosed
                # in the parentheses from 2
                stack.append(result)
                # if you store the sign at the top of the stack, you
                # can simply apply the sign directly to the result when
                # you pop it out, no need for temporary variables
                stack.append(sign)
                sign, result = 1, 0
            elif c == ")":
                # you do need to finish calculating the result inside the paren
                result += sign * num
                num = 0
                # apply the sign that was a prefix to the open paren to
                # the result found inside the paren
                result *= stack.pop()
                result += stack.pop()

        # if there is an unprocessed trailing number, we apply it to the result
        # here, and this is safe because we always reset the state of sign and
        # num when a number is processed in the parse loop
        return result + num * sign


def test_addition():
    result = Solution().calculate("1+1")
    assert result == 2


def test_subtration():
    result = Solution().calculate("2 - 1")
    assert result == 1


def test_whitespace():
    result = Solution().calculate("   2  -   1  + 1")
    assert result == 2


def test_paren_strip():
    result = Solution().calculate("(1+(4+5+2)-3)+(6+8)")
    assert result == 23


def test_empty():
    result = Solution().calculate("")
    assert result == 0


def test_multicharacter():
    result = Solution().calculate("234324234234")
    assert result == 234324234234
