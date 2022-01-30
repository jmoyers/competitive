"""
---
number: 393
title: UTF-8 Validation
difficulty: medium
tags:
- bit manipulation
- masking
- utf-8
- grapheme
- byte
- validation
links:
- https://leetcode.com/problems/utf-8-validation/
---
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0,
followed by n-1 bytes with most significant 2 bits being 10.

This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Given an array of integers representing the data, return whether it is a
valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each
integer is used to store the data. This means each integer represents only 1
byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010
00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte
character.

Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100
00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes
character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
"""
from typing import List


class Solution:
    """
    Extremely bad problem description led to convoluted function design here, 
    but I'm too lazy to fix it. Main takeaway is masking to figure out whether
    one bit is set on a byte, and using that to validate the grapheme.
    """

    def validUtf8(self, data: List[int]) -> bool:
        if len(data) < 1:
            return False

        num_bytes = 0
        bit = 8

        # btw 2**6 == (1<<6)
        # find how many bytes we're expecting
        while bit >= 1 and data[0] & (1 << bit - 1):
            num_bytes += 1
            bit -= 1

        if num_bytes == 0 and len(data) == 1:
            return True
        elif num_bytes == 0:
            return self.validUtf8(data[1:])

        if (
            num_bytes > len(data)
            or (num_bytes == 1 and len(data) >= 1)
            or num_bytes > 4
        ):
            return False

        for n in range(1, num_bytes):
            # check the two first significant bits for '10'
            if not data[n] & (1 << 7) or data[n] & (1 << 6):
                return False

        if len(data) > num_bytes:
            return self.validUtf8(data[num_bytes:])

        return True


def test_lc1():
    inp = [235, 140, 4]

    result = Solution().validUtf8(inp)

    assert result == False


def test_lc2():
    inp = [255]

    result = Solution().validUtf8(inp)

    assert result == False


def test_lc3():
    inp = [145]

    result = Solution().validUtf8(inp)

    assert result == False


def test_lc4():
    inp = [240, 162, 138, 147, 145]
    result = Solution().validUtf8(inp)

    assert result == False


def test_lc5():
    inp = [250, 145, 145, 145, 145]
    result = Solution().validUtf8(inp)

    assert result == False


def test_recurse():
    inp = [228, 189, 160, 229, 165, 189, 13, 10]
    result = Solution().validUtf8(inp)

    assert result == True


def test_lc6():
    inp = [39, 89, 227, 83, 132, 95, 10, 0]
    result = Solution().validUtf8(inp)

    assert result == False
