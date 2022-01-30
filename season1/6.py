"""
---
title:ZigZag Conversion
difficulty:medium
number:6
tags:
- parsing
- string
links:
- https://leetcode.com/problems/zigzag-conversion/
---

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this: (you may want to display this pattern in a fixed font for
better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a
number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

PINALSIGYAHRPI

P   A   H   N
A P L S I I G
Y   I   R

PAHNAPLSIIGYIR

P       H
A     S I
Y   I   R
P L     I G
A       N

PHASIYIRPLIGAN
"""


class Solution:
    """
    I think we can maintain a list of characters for each row in the output
    string and then just iterate through a zig phase and a zag phase.
    """

    def convert(self, s: str, numRows: int) -> str:
        output = [[] for i in range(numRows)]
        index = 0

        def flatten(output):
            results = ""
            for l in output:
                for c in l:
                    results += c
            return results

        while index < len(s):
            # zig
            for i in range(numRows):
                output[i].append(s[index])
                index += 1

                if index >= len(s):
                    return flatten(output)

            # zag
            for i in reversed(range(numRows - 2)):
                output[i + 1].append(s[index])
                index += 1

                if index >= len(s):
                    return flatten(output)

        return flatten(output)


def test_lc1():
    input = "PAYPALISHIRING"
    assert Solution().convert(input, 4) == "PINALSIGYAHRPI"
    assert Solution().convert(input, 3) == "PAHNAPLSIIGYIR"
    assert Solution().convert(input, 5) == "PHASIYIRPLIGAN"
