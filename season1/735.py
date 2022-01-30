"""
---
number: 735
title: Asteroid Collision
difficulty: medium
tags:
- stack
- linear
- line collision
links:
- https://leetcode.com/problems/asteroid-collision/
---
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids
meet, the smaller one will explode. If both are the same size, both will
explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.
Example 3:
Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Example 4:
Input: 
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet
each other.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
"""

from typing import List


class Solution:
    """
    Remember that when you have a collapsing single dimension, a stack is a nice
    abstraction, because it fits the interaction and makes it so you only ever
    have to look in one place for the two things you need to check in terms
    of objects interacting with each other.

    My first solution used plain iteration and tried to acct for the destruction
    of asteroids with a set, then iterate through the list. The problem comes 
    when you realize that there is a "chain reaction" where you have to start
    iterating out to the left and right. Bookkeeping is little more difficult,
    you have the option of maintaining a set (with the constant time of hashing)
    of destroyed asteroids, or being destructive with the input array you're
    given, which potentially destroying things in the middle of the array, its
    much less effecient than using a stack based approach.

    Stack just cleaner and def more efficient in every way.
    """

    def asteroidCollision(self, roids: List[int]) -> List[int]:
        stack = []

        for a in roids:
            if not stack:
                stack.append(a)
                continue

            while True:
                if stack and stack[-1] > 0 and a < 0:
                    if abs(a) > abs(stack[-1]):
                        stack.pop()
                    elif abs(stack[-1]) > abs(a):
                        break
                    else:
                        stack.pop()
                        break
                else:
                    stack.append(a)
                    break

        return stack


def test_lc1():
    inp = [10, 2, -5]
    result = Solution().asteroidCollision(inp)
    assert result == [10]


def test_lc2():
    inp = [5, 10, -5]
    result = Solution().asteroidCollision(inp)

    assert result == [5, 10]


def test_lc3():
    inp = [-2, 2, -1, -2]
    result = Solution().asteroidCollision(inp)

    assert result == [-2]


def test_lc4():
    inp = [-2, 1, -1, -1]
    result = Solution().asteroidCollision(inp)

    assert result == [-2, -1]
