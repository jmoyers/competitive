"""
---
title: Find Median from Data Stream
difficulty: hard
level: 3
tags:
- median
- stream
- sorting
- heap
- balanced heap
links: 
- https://leetcode.com/problems/find-median-from-data-stream
---
Median is the middle value in an ordered integer list. If the size of the
list is even, there is no middle value. So the median is the mean of the two
middle value.

For example,

[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data
      structure.
    double findMedian() - Return the median of all elements so far.

Follow up:

    If all integer numbers from the stream are between 0 and 100, how would you
    optimize it?

    If 99% of all integer numbers from the stream are between 0 and 100, how
    would you optimize it?
"""
import heapq


class MedianFinder:
    """
    There are two methods that I've seen for this that make the most
    intuitive sense
    
    Method 1:
        Maintain a sorted lists as new numbers come in via insertion sort (binary
        search to find insertion point, so log n). Because the data, findMedian
        is a straightforward split. This should be O(log n) for each new
        item and O(1) for finding the median
    
    Method 2:
        Maintain two balanced binary heaps, where each heap contains half the
        input. The left heap is a max heap, right heap is a min heap.
        Insertion into a heap is log n. To maintain balance between the two
        heaps, you need to exchange values from one to the other (pop and
        push) on each new input encountered. Because we have the maximum for
        the left and the minimum for the right, finding the median is simply
        peeking the top of either heap to find the median.
    
    We'll use Method 2 here
    """

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        left, right = self.heaps

        # note, we need to choose 1 heap to be larger in cases where we
        # have an odd number of inputs. we'll choose the right heap.
        # this will give the right heap the property that in cases were
        # the number of inputs is odd, the top of the right heap will be
        # the exact median

        # we add all new inputs to the right heap first. because pythons heap
        # implementation is a min heap, we don't negate the input
        heapq.heappush(right, num)

        # the next two operations are to keep the two heap sizes balanced
        # because these are min and max heaps side by side, we can use
        # that property to essentially swap the top items on the heap back
        # and forth to maintain balance - think about this carefully, this is
        # the core of this algorithm

        # by default we then want to pull out the next smallest item (heappop)
        # off the right heap and add it to the left heap. because the left
        # heap is a max heap, we negate the input because pythons heap
        # implementation is a min heap
        heapq.heappush(left, -heapq.heappop(right))

        # now, we want to make sure the heaps are balanced, so we make sure
        # to always pop an item off the top of left and give it to right
        # if left becomes larger
        if len(left) > len(right):
            heapq.heappush(right, -heapq.heappop(left))

    def findMedian(self) -> float:
        # if the right heap is larger, we have an odd number of inputs and
        # the median is simply the top of the right heap

        left, right = self.heaps

        if len(right) > len(left):
            return float(right[0])

        # otherwise we have an even number of inputs, so we take the average
        # of the two inputs on the top of either heap
        # note: we negate the left heap top because its a max heap and
        # pythons built-in is a min heap
        return (-left[0] + right[0]) / 2.0


def test_1():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert 1.5 == mf.findMedian()
    mf.addNum(3)
    assert 2.0 == mf.findMedian()
