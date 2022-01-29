"""
---
title: Meeting Rooms II
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/meeting-rooms-ii
---
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""
from typing import List
import heapq


def minMeetingRooms(intervals: List[List[int]]) -> int:
    # minimally we need to sort by start time, because we can't process this
    # in just any order. these are chronological events, and we need to create
    # a timeline to allow us to build up the # of required rooms

    # an end time signifies a room freeing up
    # a start time signifies that we require a room, but not necessarily a new room

    # as we process each individual start time, we need to consider the next
    # soonest end time for a meeting. if the next soonest end time for a meeting
    # is after the start time we're currently looking at, we need to increment
    # the number of rooms required, if not, the number of rooms required stays the
    # same

    # i will intially sort on start time, then create a priority queue
    # based on end time, so that the next soonest ending meeting will
    # be on top. you could also seperate start and end time into two arrays
    # and sort them seperately with the same effect (both O(n log n))

    rooms: int = 0

    # reverse sort on start time in place, so we can cheaply pop
    intervals.sort(key=lambda time: -time[0])

    # make a copy here, swapping end and start so we can use a py min heap
    ends: List[List[int]] = [[time[1], time[0]] for time in intervals]

    # min heap the end times
    heapq.heapify(ends)

    while intervals:
        start, _ = intervals.pop()

        # peek the next end time, if it hasn't ended yet, start up a room
        if start < ends[0][0]:
            rooms += 1
        else:
            heapq.heappop(ends)

    return rooms


result = minMeetingRooms([[15, 20], [0, 30], [5, 10]])
print(result)
assert result == 2

result = minMeetingRooms([[7, 10], [2, 4]])
print(result)
assert result == 1
