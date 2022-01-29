"""
---
title: Time Based Key-Value Store
difficulty: medium
level: 2
tags:
- bisect
- sorting
- dictionary
- hash map
- array
- time series
links: 
- https://leetcode.com/problems/time-based-key-value-store/
---
Create a timebased key-value store class TimeMap, that supports two
operations.

1. set(string key, string value, int timestamp)

    Stores the key and value, along with the given timestamp.

2. get(string key, int timestamp)

    Returns a value such that set(key, value, timestamp_prev) was called
    previously, with timestamp_prev <= timestamp. If there are multiple such
    values, it returns the one with the largest timestamp_prev. If there are no
    values, it returns the empty string ("").
"""
from typing import Dict, List

from collections import defaultdict
from bisect import bisect


class TimeMap:
    def __init__(self):
        # key -> timestamp, timestamp ascending order
        # its an OrderedDict so when we get the key list later its still
        # guaranteed to be in ascending order
        self.store: Dict[str, Dict[int, str]] = defaultdict(dict)
        self.time_store: Dict[str, List[int]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # set O(1)
        self.store[key][timestamp] = value
        self.time_store[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        # O(log n) binary search to find the next largest time or exact the
        # time we're after

        if key not in self.store:
            return ""

        index = bisect(self.time_store[key], timestamp)

        # 1 2 3 4 6
        # 5 -> 4
        # 1 2 3 4 5 6
        #       ^

        if 0 <= index - 1 < len(self.time_store[key]):
            return self.store[key][self.time_store[key][index - 1]]

        return ""


def test_1():
    tm = TimeMap()

    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"
    tm.set("foo", "bar2", 4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"


#
# Example 2:
#
# Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
# Output: [null,null,null,"","high","high","low","low"]
