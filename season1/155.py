"""
---
title: Min Stack
difficulty: easy
level: 1
links: 
- https://leetcode.com/problems/min-stack
---
"""


class MinStack:
    """
    The key is a dynamic programming solution whereby, since we
    don't actually need to remove the minimum value (as would
    be the case in the much more common data structure min binary
    heap), we can collapse the minimum and store it at each index
    with the value to be stored on the stack.
 
    We'll use tuple, the first being the minimum, the second being
    the value.
 
    If we encounter a new minimum, all values ABOVE this item on the
    stack will be paired with this new min from now on, until such
    time as we encounter an even smaller value.
 
    In this way, when we pop, we'll maintain a history of the 
    smallest values as we rewind in time.
    """

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            min_val = min(self.stack[-1][0], x)
            self.stack.append((min_val, x))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]


def test_lc1():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2
