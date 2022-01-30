"""
---
title: LFU Cache
number: 460
tags:
- cache
- lfu
- lfu cache
---
Design and implement a data structure for Least Frequently Used (LFU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least
frequently used item before inserting a new item. For the purpose of this
problem, when there is a tie (i.e., two or more keys that have the same
frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the
get and put functions for that item since it was inserted. This number is set
to zero when the item is removed.


Follow up:
Could you do both operations in O(1) time complexity?
 

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ )

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # returns 1
cache.put(3, 3)    # evicts key 2
cache.get(2)       # returns -1 (not found)
cache.get(3)       # returns 3.
cache.put(4, 4)    # evicts key 1.
cache.get(1)       # returns -1 (not found)
cache.get(3)       # returns 3
cache.get(4)       # returns 4

"""

from collections import OrderedDict


class Node:
    def __init__(self, val):
        self.val = val
        self.freq = 0


class LFUCache:
    """
    For O(logn) I think we need 3 data structures...
    - dictionary for storing values

    - combined
        - dictionary for storing frequency of access and pointing to heap entry
        - min heap for storing the next-to-reject cache entry
    
    When you need to update a the frequency of an item, you can use the
    dictionary that points key -> heap entry, update the value, and restore
    the heap invariant. This should take logn. Hmm, this isn't O(1)!

    For O(1), we need to maintain...
    - dictionary for storing values
    - an array of doubly linked lists storing freq -> List[Node]
        - this is so we can remove an item from the list in O(1)
        - say we just retrieved an item from our store, we need to increment
            its freqency
            - starts with frequency 0
            - increment frequency 1
            - remove node from frequency 0 list, using dict key -> value, which
                references the node directly. with just the node we can remove
                it from the linked list
            - add to frequency 1 list

        Instead of a doubly linked list, we can use an OrderedDict for each
        frequency entry, and wrap the values in a class that stores the value
        and the frequency for which it is accessed. We can then get the
        appropriate frequency array from this frequency number, and access the
        dictionary by key and manipulate it.

    For cache ejection, we take the end of the ordered dict for the smallest
    known frequency. We can keep track of the smallest known frequency to keep
    the acces O(1)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.vstore = {}
        self.fstore = OrderedDict()
        self.fstore[0] = OrderedDict()
        self.minf = 0
        self.ejected = []

    def debug(self):
        results = []
        counts = []

        for l in self.fstore.values():
            for i in l:
                results.append(i)

        for f in self.fstore:
            counts.append((f, len(self.fstore[f])))

        return (self.minf, results, counts)

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # update value and frequency for item seen
        if key in self.vstore:
            node = self.vstore[key]

            del self.fstore[node.freq][key]

            if self.minf == node.freq and len(self.fstore[node.freq]) == 0:
                self.minf += 1

            node.val = value
            node.freq += 1

            if node.freq not in self.fstore:
                self.fstore[node.freq] = OrderedDict()

            self.fstore[node.freq][key] = node
        else:
            node = Node(value)

            self.vstore[key] = node

            # eject if necessary
            if len(self.vstore) > self.capacity:
                (removed_key, _) = self.fstore[self.minf].popitem(last=False)
                del self.vstore[removed_key]

            self.fstore[node.freq][key] = node
            self.minf = 0

    def get(self, key: int) -> int:
        if key not in self.vstore:
            return -1

        node = self.vstore[key]

        del self.fstore[node.freq][key]

        if self.minf == node.freq and len(self.fstore[node.freq]) == 0:
            self.minf += 1

        node.freq += 1

        if node.freq not in self.fstore:
            self.fstore[node.freq] = OrderedDict()

        self.fstore[node.freq][key] = node

        return node.val


def test_lc1():
    cache = LFUCache(2)

    cache.put(1, 1)
    print(cache.debug())
    cache.put(2, 2)
    print(cache.debug())
    assert cache.get(1) == 1
    print(cache.debug())
    cache.put(3, 3)  # evicts key 2
    print(cache.debug())
    assert cache.get(2) == -1
    print(cache.debug())
    # 1 and 3 have even freq, but this was accessed more recently
    assert cache.get(3) == 3
    print(cache.debug())
    cache.put(4, 4)  # evicts key 1.
    print(cache.debug())
    assert cache.get(1) == -1
    print(cache.debug())
    assert cache.get(3) == 3
    print(cache.debug())
    assert cache.get(4) == 4
    print(cache.debug())


def test_lc2():
    cache = LFUCache(2)

    cache.put(3, 1)
    cache.put(2, 1)
    cache.put(2, 2)
    cache.put(4, 4)


def test_lc3():
    c = LFUCache(10)

    inp = [
        "put",
        "put",
        "put",
        "put",
        "put",
        "get",
        "put",
        "get",
        "get",
        "put",
        "get",
        "put",
        "put",
        "put",
        "get",
        "put",
        "get",
        "get",
        "get",
        "get",
        "put",
        "put",
        "get",
        "get",
        "get",
        "put",
        "put",
        "get",
        "put",
        "get",
        "put",
        "get",
        "get",
        "get",
        "put",
        "put",
        "put",
        "get",
        "put",
        "get",
        "get",
        "put",
        "put",
        "get",
        "put",
        "put",
        "put",
        "put",
        "get",
        "put",
        "put",
        "get",
        "put",
        "put",
        "get",
        "put",
        "put",
        "put",
        "put",
        "put",
        "get",
        "put",
        "put",
        "get",
        "put",
        "get",
        "get",
        "get",
        "put",
        "get",
        "get",
        "put",
        "put",
        "put",
        "put",
        "get",
        "put",
        "put",
        "put",
        "put",
        "get",
        "get",
        "get",
        "put",
        "put",
        "put",
        "get",
        "put",
        "put",
        "put",
        "get",
        "put",
        "put",
        "put",
        "get",
        "get",
        "get",
        "put",
        "put",
        "put",
        "put",
        "get",
        "put",
        "put",
        "put",
        "put",
        "put",
        "put",
        "put",
    ]
    args = [
        [10, 13],
        [3, 17],
        [6, 11],
        [10, 5],
        [9, 10],
        [13],
        [2, 19],
        [2],
        [3],
        [5, 25],
        [8],
        [9, 22],
        [5, 5],
        [1, 30],
        [11],
        [9, 12],
        [7],
        [5],
        [8],
        [9],
        [4, 30],
        [9, 3],
        [9],
        [10],
        [10],
        [6, 14],
        [3, 1],
        [3],
        [10, 11],
        [8],
        [2, 14],
        [1],
        [5],
        [4],
        [11, 4],
        [12, 24],
        [5, 18],
        [13],
        [7, 23],
        [8],
        [12],
        [3, 27],
        [2, 12],
        [5],
        [2, 9],
        [13, 4],
        [8, 18],
        [1, 7],
        [6],
        [9, 29],
        [8, 21],
        [5],
        [6, 30],
        [1, 12],
        [10],
        [4, 15],
        [7, 22],
        [11, 26],
        [8, 17],
        [9, 29],
        [5],
        [3, 4],
        [11, 30],
        [12],
        [4, 29],
        [3],
        [9],
        [6],
        [3, 4],
        [1],
        [10],
        [3, 29],
        [10, 28],
        [1, 20],
        [11, 13],
        [3],
        [3, 12],
        [3, 8],
        [10, 9],
        [3, 26],
        [8],
        [7],
        [5],
        [13, 17],
        [2, 27],
        [11, 15],
        [12],
        [9, 19],
        [2, 15],
        [3, 16],
        [1],
        [12, 17],
        [9, 1],
        [6, 19],
        [4],
        [5],
        [5],
        [8, 1],
        [11, 7],
        [5, 2],
        [9, 28],
        [1],
        [2, 2],
        [7, 4],
        [4, 22],
        [7, 24],
        [9, 26],
        [13, 28],
        [11, 26],
    ]

    results = [
        None,
        None,
        None,
        None,
        None,
        -1,
        None,
        19,
        17,
        None,
        -1,
        None,
        None,
        None,
        -1,
        None,
        -1,
        5,
        -1,
        12,
        None,
        None,
        3,
        5,
        5,
        None,
        None,
        1,
        None,
        -1,
        None,
        30,
        5,
        30,
        None,
        None,
        None,
        -1,
        None,
        -1,
        24,
        None,
        None,
        18,
        None,
        None,
        None,
        None,
        14,
        None,
        None,
        18,
        None,
        None,
        11,
        None,
        None,
        None,
        None,
        None,
        18,
        None,
        None,
        -1,
        None,
        4,
        29,
        30,
        None,
        12,
        11,
        None,
        None,
        None,
        None,
        29,
        None,
        None,
        None,
        None,
        17,
        -1,
        18,
        None,
        None,
        None,
        -1,
        None,
        None,
        None,
        20,
        None,
        None,
        None,
        29,
        18,
        18,
        None,
        None,
        None,
        None,
        20,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]

    results = list(reversed(results))

    for i, method in enumerate(inp):
        r = results.pop()
        if getattr(c, method)(*(args[i])) != r:
            print("Bad stuff")
            print(method, args[i], r)
            exit()
        print(method, args[i])
        print(c.debug())
        print()

