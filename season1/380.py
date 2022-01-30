"""
---
title: Insert Delete GetRandom O(1)
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/insert-delete-getrandom-o1
---
Design a data structure that supports all following operations in average
O(1) time.

    insert(val): Inserts an item val to the set if not already present.
    remove(val): Removes an item val from the set if present.
    getRandom: Returns a random element from current set of elements (it's
    guaranteed that at least one element exists when this method is called). Each
    element must have the same probability of being returned.

Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""
from random import choice


class RandomizedSet:
    """
    For O(1) random get, our choices are List
    For O(1) insert, our choices are Hash, List
    For O(1) delete, our choices are Hash. Because we're requiring a List for
        O(1) random get, we'll need to support a List as well. To do this
        we'll need to store the index of each item in our Hash -> List. With
        this information we can do an O(1) delete. Specifically, you have an
        extra swap operation, once you get the index of the item to delete,
        to avoid O(n) memmove you need to swap the item to delete to the last
        index and pop it off. We can do this because there is no guaranteed
        order.
    """

    def __init__(self):
        self.list = []
        self.hash = {}

    def insert(self, val):
        if val not in self.hash:
            self.list += [val]
            self.hash[val] = len(self.list) - 1
            return True
        else:
            return False

    def remove(self, val):
        if val in self.hash:
            index = self.hash[val]

            # swap our item to delete to the last index and pop it off
            self.list[-1], self.list[index] = self.list[index], self.list[-1]

            # do update the index for the swapped item
            self.hash[self.list[index]] = index

            self.list.pop()
            self.hash.pop(val)

            return True

        return False

    def getRandom(self):
        return choice(self.list)


def test_leetcode1():
    rs = RandomizedSet()
    rs.insert(0)
    rs.insert(1)
    rs.remove(0)
    rs.insert(2)
    rs.remove(1)
    assert rs.getRandom() == 2


def test_insert_remove():
    rs = RandomizedSet()
    rs.insert(5)
    rs.insert(6)

    assert len(rs.list) == 2
    assert len(rs.hash) == 2
    assert rs.hash[5] == 0
    assert rs.getRandom() in (5, 6)

    rs.remove(5)

    assert len(rs.list) == 1
    assert len(rs.hash) == 1

    assert rs.getRandom() == 6
