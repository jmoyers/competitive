"""
---
title: Container With Most Water
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/container-with-most-water
---
Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with
x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
this case, the max area of water (blue section) the container can contain is
49.

"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # This is an area problem that doesn't consider items in between the
        # two selected indexes. Therefore we can use a two pointer solution that
        # starts on the outer edges

        # If we continually move the pointer that is pointing to the shorter of the
        # two edges inward, we can guarantee that we'll always be dismissing
        # a potentially smaller area

        # Intuitions that came to mind at first that aren't correct:
        # Is this a dynamic programming problem where we can look left and consider
        # only the maximum line to the left of the current index? No, because
        # there could be an extremely wide and short container that would surpass
        # the area trapped by a tall narrow container
        # Can we consider some local greedy solution and somehow use that to apply
        # some sort/dismiss a large number of inputs? Doesn't seem applicable,
        # because again, both axis are important in the solution.

        # However, if we start our solution maximally along one axis (the x-axis)
        # in this case, we can then isolate and dismiss one option at a time by
        # examining the other axis (the shorter line is examining the y-axis)

        l: int = 0
        r: int = len(height) - 1
        area: int = -1

        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area


result = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)
assert result == 49
