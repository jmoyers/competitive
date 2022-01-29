"""
---
title: Set Intersection Size At Least Two
difficulty: hard
level: 3
tags:
- line sweep
- intervals
- events
links: 
- https://leetcode.com/problems/set-intersection-size-at-least-two
---
We are given a list schedule of employees, which represents the working time
for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals
are in sorted order.

Return the list of finite intervals representing common, positive-length free
time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects
inside are Intervals, not lists or arrays. For example, schedule[0][0].start
= 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined). Also, we
wouldn't include intervals like [5, 5] in our answer, as they have zero
length.

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.

Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]

 

Constraints:

    1 <= schedule.length , schedule[i].length <= 50
    0 <= schedule[i].start < schedule[i].end <= 10^8
"""

from typing import List
from enum import Enum


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __hash__(self):
        return hash(f"{self.start},{self.end}")


class Event(Enum):
    START = 0
    STOP = 1


class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        """
        We can use a technique here called a line sweep. If we convert the list
        of intervals into a sorted list of start and end intervals for all
        employees and treat them like events, then we count how many overlapping
        start events for a given time (a balance). When the balance hits 0, we
        record the start of an open time interval. When the balance then reaches
        non-zero, we can close the interval and append it to the list.
        """

        events = []

        for emp in schedule:
            for interval in emp:
                events.append((interval.start, Event.START))
                events.append((interval.end, Event.STOP))

        # sort by time only, not event type
        events.sort(key=lambda e: e[0])

        last = None
        working = 0
        open = []

        for e in events:
            if e[1] == Event.START:
                if working == 0 and last is not None and e[0] - last > 0:
                    open.append(Interval(last, e[0]))
                working += 1
            if e[1] == Event.STOP:
                working -= 1
                last = e[0]

        return open

    def findOccupied(self, schedule: List[List[Interval]]) -> List[Interval]:
        """
        This one is doable, same time complexity, but more complicated in code.

        I think the datastructure we want to examine at the end of processing
        employee schedules is a flattened list of sorted occupied intervals,
        and then the answer we return is the inverse of this, sans non-finite
        answers.

        So we need a central datastructure to store intervals. Intervals
        are mutable.

        First pass:
        Grab all the intervals from first employees, put them in our collapsed
        list verbatim. I assume these Intervals can't overlap with each other.
        If they do, we'll have to modify to something more like second pass
        below.

        Second pass:
        Examine if the start time of a given interval is inside one the existing
        intervals in the central store. If so, set the end time to max()
        The brute force approach here is to iterate from the sorted start to
        end and find the target interval.

        The second thing we have to consider is if the new end time is now
        overlapping with the start time for any interval after itself. If it
        is, we have to gobble up the intervals in front of us until endTime <
        startTime of next interval.

        The above looks like some sort of n ^ m >= because we need to examine
        at most max(intervals) for all employees (m) n times where n is employees.

        In theory we could have a sorted list of starts referring to the index
        of their source interval, then we could use log n search to find.

        Then you could have a sorted lists of ends referring back to index, so
        you could find the END target index in another log n search. Then you
        could combine all the intervals in between start and end.

        This would make it n * 2 log m
        """
        pass


def test_1():
    schedule = [
        [Interval(1, 3), Interval(6, 7)],
        [Interval(2, 4)],
        [Interval(2, 5), Interval(9, 12)],
    ]

    out = [Interval(5, 6), Interval(7, 9)]

    result = Solution().employeeFreeTime(schedule)

    assert set(result) == set(out)

