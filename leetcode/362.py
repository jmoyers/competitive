"""
---
title: Design Hit Counter
difficulty: medium
number: 362
tags: 
- scale
- hit counter
- time series
- design
- binary search
- dictionary
- hash table
- ordered dictionary
- bisect
---

Design a hit counter which counts the number of hits received in the past 5
minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may
assume that calls are being made to the system in chronological order (ie, the
timestamp is monotonically increasing). You may assume that the earliest
timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1. counter.hit(1);

// hit at timestamp 2. counter.hit(2);

// hit at timestamp 3. counter.hit(3);

// get hits at timestamp 4, should return 3. counter.getHits(4);

// hit at timestamp 300. counter.hit(300);

// get hits at timestamp 300, should return 4. counter.getHits(300);

// get hits at timestamp 301, should return 3. counter.getHits(301); 

Follow up: What if the number of hits per second could be very large? Does your
design scale?
"""

from collections import OrderedDict
import bisect


class HitCounter:
    """
    The simplest solution is to store all hit timestamps in a list.
    Then when you request the last 5 minutes, you find the target timestamp
    (now - 5 minutes), find it via binary search and sum all the entries from
    that index forward.

    If the number of hits per second is large, you probably don't want to store
    duplicate timestamp entries in your list, so you could use an Ordered 
    Dictionary of to store a counter for a given second. This incurs a constant
    cost of hashing, which can be the limiting factor for thru-put.

    """

    def __init__(self):
        self.store = OrderedDict()

    def hit(self, timestamp: int) -> None:
        if timestamp in self.store:
            self.store[timestamp] += 1
        else:
            self.store[timestamp] = 1

    def getHits(self, timestamp: int) -> int:
        target = timestamp - (5 * 60)
        timestamps = list(self.store.keys())
        index = bisect.bisect_right(timestamps, target)
        total = 0
        for i in range(index, len(timestamps)):
            total += self.store[timestamps[i]]
        return total


def test_1():
    counter = HitCounter()

    counter.hit(1)
    counter.hit(2)
    counter.hit(3)

    assert counter.getHits(4) == 3

    counter.hit(300)

    assert counter.getHits(300) == 4
    assert counter.getHits(301) == 3
