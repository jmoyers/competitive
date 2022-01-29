"""
---
number: 218
title: The Skyline Problem
difficulty: hard
tags:
- line sweep
- interval
- max heap
- min heap
- heap delete
links:
- https://leetcode.com/problems/the-skyline-problem/
---
A city's skyline is the outer contour of the silhouette formed by all the
buildings in that city when viewed from a distance. Now suppose you are given
the locations and height of all the buildings as shown on a cityscape photo
(Figure A), write a program to output the skyline formed by these buildings
collectively (Figure B).

Buildings Skyline Contour The geometric information of each building is
represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x
coordinates of the left and right edge of the ith building, respectively, and
Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤
INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles
grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [
[2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of
[ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key
point is the left endpoint of a horizontal line segment. Note that the last
key point, where the rightmost building ends, is merely used to mark the
termination of the skyline, and always has zero height. Also, the ground in
between any two adjacent buildings should be considered part of the skyline
contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3
15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].
Notes:

The number of buildings in any input list is guaranteed to be in the range [0,
10000].

The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.

There must be no consecutive horizontal lines of equal height in the output
skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not
acceptable; the three lines of height 5 should be merged into one in the
final output as such: [...[2 3], [4 5], [12 7], ...]
"""

import heapq
from collections import defaultdict
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        # make our buildings list into an array of events where
        # start = (x, height)
        # end = (x, height)

        # n log n
        # sort events on x

        # log n
        # at every new start, we add our height into a max heap
        # if the top of the max heap changed, we add a critical point at x, height

        # log n - if we're lazy its log n, if we just re-heapify its o n
        # on every end event, delete the height from the max heap
        # if the max height changed as a result, add a critical point at x, height

        events = []

        start_event, end_event = 0, 1

        max_heap = [0]

        for b in buildings:
            events.append((b[0], start_event, b[2]))
            events.append((b[1], end_event, b[2]))

        events = sorted(events)

        deleted = defaultdict(lambda: 0)
        key_points = []

        for e in events:
            if e[1] == start_event:
                old_max = -max_heap[0]

                heappush(max_heap, -e[2])

                while deleted[-max_heap[0]] > 0:
                    deleted[-max_heap[0]] -= 1
                    heappop(max_heap)

                if old_max != -max_heap[0]:
                    if (
                        key_points
                        and key_points[-1][0] == e[0]
                        and key_points[-1][1] < e[2]
                    ):
                        key_points[-1] = [e[0], e[2]]
                    else:
                        key_points.append([e[0], e[2]])

            if e[1] == end_event:
                deleted[e[2]] += 1

                old_max = -max_heap[0]

                while deleted[-max_heap[0]] > 0:
                    deleted[-max_heap[0]] -= 1
                    heappop(max_heap)

                if old_max != -max_heap[0]:
                    if (
                        key_points
                        and key_points[-1][0] == e[0]
                        and key_points[-1][1] > -max_heap[0]
                    ):
                        key_points[-1] = [e[0], -max_heap[0]]
                    else:
                        key_points.append([e[0], -max_heap[0]])

        return key_points

