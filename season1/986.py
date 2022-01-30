"""
---
title: Interval List Intersections
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/interval-list-intersections/
tags:
- line sweep
- interval
- list
- array
- tuple
- event
---
Given two lists of closed intervals, each list of intervals is pairwise
disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real
numbers x with a <= x <= b. The intersection of two closed intervals is a set
of real numbers that is either empty, or can be represented as a closed
interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
"""

from typing import List


class Solution:
    """
    For each of intervals you can have a start and stop event.

    a[0] = start event
    a[1] = end event
    2 events in our events system

    b[0] = start event
    b[1] = end event
    Also 2 events.

    Sort the events. Implies n log n.

    Process the events. Whenever you hit a start event, add 1 to the
    overlap (one variable). Whenever you hit an end event, substract from
    the overlap. What you're looking for is overlap == 2. Whenever
    overlap == 2, start an overlapped interval, and whenever it dips
    below 2, end the overlapped interval. Keep a results array to push
    the intervals into on close. Line scan algorithm

    Time complexity: n * log(n)
    """

    def intervalIntersection(
        self, A: List[List[int]], B: List[List[int]]
    ) -> List[List[int]]:
        events = []
        for item in A:
            if item[0] == item[1]:
                continue
            start_event = (item[0], 0)
            end_event = (item[1], 1)
            events.append(start_event)
            events.append(end_event)

        for item in B:
            if item[0] == item[1]:
                continue
            start_event = (item[0], 0)
            end_event = (item[1], 1)
            events.append(start_event)
            events.append(end_event)

        events.sort()

        overlapped = 0
        current_interval = None
        result = []

        for time, type in events:
            if type == 0:
                overlapped += 1
            elif type == 1:
                overlapped -= 1
            if overlapped == 2:
                current_interval = [time, None]
            if current_interval and overlapped < 2:
                current_interval[1] = time
                result.append(current_interval)
                current_interval = None

        return result


def test_lc1():
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    out = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    result = Solution().intervalIntersection(A, B)
    assert result == out
