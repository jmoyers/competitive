"""
---
number: 1229
title: Meeting Scheduler
difficulty: medium
tags:
- line sweep
- interval
links:
- https://leetcode.com/problems/meeting-scheduler/
---

Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.  

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

 

Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []
 

Constraints:

1 <= slots1.length, slots2.length <= 10^4
slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1]
slots2[i][0] < slots2[i][1]
0 <= slots1[i][j], slots2[i][j] <= 10^9
1 <= duration <= 10^6 
"""

import math
from typing import List


class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        """
        start events
        end events
        
        sort events by time
        (time, event_type = 0 start, 1 end)
        
        open_slots
        
        when open_slots hits 2, we record start_time
        when open_slots goes below 2, we check end_time - start_time > duration,
            return start_time, start_time + duration        
        """

        events = []
        start_event, end_event = 0, 1

        for slot in slots1:
            events.append((slot[0], start_event))
            events.append((slot[1], end_event))

        for slot in slots2:
            events.append((slot[0], start_event))
            events.append((slot[1], end_event))

        # o log n
        events = sorted(events)

        open_slots = 0
        start_time = math.inf

        for event in events:
            if event[1] == start_event:
                open_slots += 1
                if open_slots == 2:
                    start_time = event[0]
            else:
                if open_slots == 2:
                    open_duration = event[0] - start_time
                    if open_duration >= duration:
                        return [start_time, start_time + duration]
                    else:
                        start_time = math.inf
                open_slots -= 1

        return []
