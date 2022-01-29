"""
---
number:767
title:Reorganize String
difficulty:medium
tags:
- heap
- frequency map
- parsing
- interleaving
links:
- https://leetcode.com/problems/reorganize-string/
---
Given a string S, check if the letters can be rearranged so that two
characters that are adjacent to each other are not the same.

If possible, output any possible result. If not possible, return the empty
string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""


from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    """
    I had some trouble with this one at the beginning. I had the right general
    concept -- count characters, interleave characters, there was some math
    to determine early if it was not possible.

    However, I attempted to use an unsorted stack and it made the loop logic
    extremely complicated and convuluted. I think I could have made it work,
    but in general I think a heap or a sorted stack approach from the beginning
    would have made for much simpler to understand code.

    So, I switched to a heap alternative implementation. The only tricky bit
    is really realizing that even with a heap, you need to potentially pop
    2 items off, because the most frequent item could be the same as the 
    character at the top of the result string.

    Also key was realizing you shouldn't necessarily continuously process a 
    given character until its at a 1 count, this made the loop needlessly
    complex. You can simply re-add the character on to the heap and take the
    log n hit for correcting the heap. This vastly simplifies bookkeeping, bc
    you don't have a bunch of auxiliary structures and loop exit conditions
    to keep track of -- its simply, is there something left in the heap? Yes.
    """

    def reorganizeString(self, S: str) -> str:
        freq = Counter(S)

        heap = []
        result = ""

        # unsorted just yet
        for c, count in freq.items():
            heap.append((-count, c))

        heapify(heap)

        # ccc aaaaa
        # acacaca_ <== not enough characters to interleave between all the a's

        # if you have too many of one type of caracter such that you don't
        # have enough alternatives to interleave between the duplicates,
        # you can't possibly have a valid string
        if -heap[0][0] * 2 - 1 > len(S):
            return ""

        while heap:
            count, c = heappop(heap)

            # we can use the top of the max heap because it wouldn't result
            # in a duplicate character in the string
            if not result or result[-1] != c:
                result += c
                # reversed condition due to min/max heap flip
                if count != -1:
                    heappush(heap, (count + 1, c))
            # we can't use the top, so we use the second value out of the heap
            # and push the first back in to avoid duplication
            else:
                second_count, second_c = heappop(heap)
                heappush(heap, (count, c))

                result += second_c

                if second_count != -1:
                    heappush(heap, (second_count + 1, second_c))

        return result


def verify_output(inp, specific=None):
    result = Solution().reorganizeString(inp)

    if specific != None:
        assert specific == result
        return

    assert Counter(result) == Counter(inp)

    last = None
    for c in result:
        if c == last:
            assert False
        last = c


def test_lc1():
    verify_output("aaab", "")


def test_lc2():
    verify_output("aab")


def test_lc3():
    verify_output("aaabbb")


def test_lc4():
    verify_output("baabb")


def test_lc5():
    verify_output("zhmyo")


def test_lc6():
    verify_output("eqmeyggvp")
