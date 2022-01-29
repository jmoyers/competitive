"""
---
number: 739
title: Daily Temperatures
difficult: medium
tags:
- stack
- invariant
- monotonically increasing
- monotonic
links:
- https://leetcode.com/problems/daily-temperatures/
---

2916

90

Add to List

Share
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
from typing import List
"""

from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        The key to this problem is understanding that if you reverse process it, you're
        going to know about the next warmer temperature by virtue of already having
        processed it.
        
        Every time in reverse, if you encounter a temperature that is warmer than
        all the others that you've encountered so far, we can discard our history of
        temperatures, because they're no longer valid. We don't care about temperatures
        later in a cycle if we found the hottest peak so far.
        
        The other insight is that you want the next warmest temperature. So, if you
        noodle on it, you can figure that a stack would be an appropriate data structure
        because as you process it in reverse, the "next" warmest value will always be 
        in the stack in order via popping. If the stack is empty, there is no warmer
        temperature for this index. Since you're popping off cooler values than your
        current index, you're maintaining the invariant that we only care about temperatures
        warmer than the current index. In this way the stack can also be thought of as
        a monotonically increasing (based on temperature) array of indexes. At each
        step we're essentially correcting for this invariant, and when we find the place
        in the stack where this temperature belongs, i.e. the temperature at the top of the
        stack is larger than the one we're examining, we push the temperature that we're examining
        onto the stack.
        """

        ans = [0] * len(T)

        stack = []

        for i in reversed(range(len(T))):
            # get rid of all the temperatures in the stack colder than our
            # current temp. they are no longer relevant
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()

            # there is no answer if the stack is empty
            # our new temperature is the highest we've seen
            if stack:
                ans[i] = stack[-1] - i

            # always add current temperature to the stack. however
            # stack is not always empty. temps in the stack in behind
            # our current value are simply warmer

            # we keep the warmer values because our next temp examined
            # could be hotter than current T[i], and our current T[i]
            # might not be relvant, so we'd pop it off in above while
            stack.append(i)

        return ans


def test_1():
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    assert Solution().dailyTemperatures(T) == [1, 1, 4, 2, 1, 1, 0, 0]
