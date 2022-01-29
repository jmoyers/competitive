"""
---
title: Minimum Window Substring
difficulty: hard
level: 3
tags:
- string
- shortest path
- deque
- frequency counter
- dictionary
- hash map
- multiple pointers
links: 
- https://leetcode.com/problems/minimum-window-substring
---
Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).


Note:

    If there is no such window in S that covers all characters in T, return the
    empty string "". If there is such window, you are guaranteed that there will
    always be only one unique minimum window in S.
"""
from collections import Counter, deque
from typing import Deque, List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # start and end pointer, increment end pointer until we
        # find one instance of all required characters

        # once we do, we can increment start until we find
        # a character in set t to start on, then go back to
        # incrementing the end pointer

        # use a frequency counter on t, decrement t[character]
        # every time we come across a new character. this
        # will take care of duplicate characters in t and if we
        # leave one behind by moving the start pointer forward
        # we can increment again

        start, end = 0, 0
        next_start: Deque[int] = deque()
        min_window = ""

        counter = len(t)
        freq = Counter(t)

        # not strictly necessary to have another set, can use
        # freq counter alone, but this allows us to easily track
        # the next start index
        search = set(t)

        for end in range(len(s)):
            if s[end] in search:
                next_start.append(end)
                # we only decrement counter if we still require
                # one of these characters to satisfy window req
                if freq[s[end]] > 0:
                    counter -= 1
                freq[s[end]] -= 1

            # once we've seen all characters, possibly record
            # the minimum window. also move start forward to either
            # the next recorded character in t
            while counter == 0:
                window = end - start + 1

                if min_window == "" or len(min_window) > window:
                    min_window = s[start : end + 1]

                # a left increment produced optimal solution
                if len(next_start) == 0:
                    return min_window

                if s[start] in search:
                    freq[s[start]] += 1
                    if freq[s[start]] > 0:
                        counter += 1

                candidate = next_start.popleft()

                # special case: 1 character search string
                if len(next_start) == 0 and candidate == start:
                    return min_window

                if candidate == start:
                    candidate = next_start.popleft()

                start = candidate

        return min_window


result = Solution().minWindow("ab", "b")
print(result)
assert result == "b"

result = Solution().minWindow("ADOBECODEBANC", "ABC")
print(result)
assert result == "BANC"

result = Solution().minWindow("a", "aa")
print(result)
assert result == ""


result = Solution().minWindow("a", "a")
print(result)
assert result == "a"

result = Solution().minWindow("ab", "a")
print(result)
assert result == "a"

result = Solution().minWindow("bba", "ab")
print(result)
assert result == "ba"

result = Solution().minWindow("aaflslflsldkalskaaa", "aaa")
print(result)
assert result == "aaa"
