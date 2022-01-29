"""
---
title: Design HashMap
number: 706
tags:
- hash map
- modulo
- linked list
links:
- https://stackoverflow.com/questions/327311
- https://leetcode.com/problems/design-hashmap/
- https://stackoverflow.com/questions/13595767
---
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

    put(key, value) : Insert a (key, value) pair into the HashMap. If the
    value already exists in the HashMap, update the value.

    get(key): Returns the value to which the specified key is mapped, or -1
    if this map contains no mapping for the key.

    remove(key) : Remove the mapping for the value key if this map contains
    the mapping for the key.


Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 


Note:

    All keys and values will be in the range of [0, 1000000].
    The number of operations will be in the range of [1, 10000].
    Please do not use the built-in HashMap library.
"""


class MyHashMap:
    """
    Parts of a hash map:
    - Initial storage -- usually an array of some adjustable bucket size (M)
    - Hashing function -- turn your key into a number with good distribution
    - Compressor -- take the output of your hashing function and turn it
        into a valid array index in your storage
    
    Give the nature of a hash table, your initial array size is usually smaller
    than the range of all keys you could put in it. So when you compress your
    hashed key down to an index of size M, you need to be able to store multiple
    values in that index slot (collision). You can use a variety of data
    structures for this (array, linked list, another hash table) and there are
    trade-offs for each.

    1. array - arrays have a predetermined size initially in most impl. when
        they grow beyond their requirements they usually double in size. so
        this is a particularly memory intensive approach. the upside is you
        could store the bucketed data sorted and use a binary search if your
        bucket length is long (though I think you are trying to minimize
        collisions, so I think this is an anti goal)
    2. linked list - requires a linear search through the bucket to find the
        target key, but only grows one node at a time, so the memory
        requirements are smaller

    """

    def __init__(self):
        # lazy man, use array
        self.m = 1000
        self.store = [[] for _ in range(self.m + 1)]

    def put(self, key: int, value: int) -> None:
        # non-negative v

        # we're not even going to hash the input, its suitable for modulus
        # already, though clearly this won't give us a good distribution
        index = key % self.m

        target = self.store[index]

        if len(target) == 0:
            target.append((key, value))
        else:
            for i, (k, v) in enumerate(target):
                # the update case
                if k == key:
                    target[i] = (key, value)
                    return
            # key doesn't exist yet
            target.append((key, value))

    def get(self, key: int) -> int:
        # -1 if not in hm
        index = key % self.m

        if index >= len(self.store) or len(self.store[index]) == 0:
            return -1

        target = self.store[index]

        for (k, v) in target:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        index = key % self.m

        target = self.store[index]

        for i, (k, _) in enumerate(target):
            if k == key:
                del target[i]
                return


def test_put_get():
    hm = MyHashMap()

    hm.put(0, 10)
    assert hm.get(0) == 10

    hm.put(3, 13)
    assert hm.get(3) == 13


def test_put_remove():
    hm = MyHashMap()

    hm.put(0, 10)
    assert hm.get(0) == 10

    hm.put(3, 13)
    assert hm.get(3) == 13

    hm.remove(0)

    assert hm.get(0) == -1
    assert hm.get(3) == 13
