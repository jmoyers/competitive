"""
---
title: Sliding Window Maximum
difficulty: hard
level: 3
links: 
- https://leetcode.com/problems/sliding-window-maximum
tags:
- deque
- monotonic
---
Given an array nums, there is a sliding window of size k which is moving from
the very left of the array to the very right. You can only see the k numbers
in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

 

Constraints:

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length
"""

from typing import List, Deque
from collections import deque


class Solution:
    """
    Simplest solution should be O(nk), just iterate over the list starting at
    index 0, iterate k items forward, finding the maximum, push result into
    answer list, repeat for len(nums)

    Linear time:

    If we can keep track of the index of the second highest value as well
    as the max value from the current window, and make sure we discard
    them appproriately when the window shifts, we can do this in linear time.

    We use a double ended queue of size k. We are essentially maintain a 
    `monotonic array` which has the useful property of retaining the general
    structure of the input data, but only keeping the relevant information for
    later in the problem (i.e. the next largest max will be the next item
    in the monotonic array after we shift the previous max off the front of
    the queue when the window shifts). Monotonically decreasing like 4, 4, 3, 2
    and so on.

    Invariant: the front of the queue has the largest value seen for this window

    So, once you've processed all the items in this window, invariably you
    will find the largest element for the window at deque[0] and can use that
    to build the final output.

    So we maintain this invariant by:
        1. When you encounter a new value, you want to look at the back of
        the queue. If your current element is larger, discard the item on
        the back of the queue -- this is because this element is not a candidate
        for being a maximum value to a later window, i.e. this new value 
        supercedes it as a potential maximum to later windows by virtue of it
        being to the right of it AND also larger. Therefore that element is
        never again relevant, and we discard it. We repeat this process until
        either queue is empty or the current item is not larger than the element
        next up at the back of the queue.

        2. Regardless of whether you've discarded the element or not, you
        push the element onto the back of the queue. This is because, due to the
        fact that it is to the RIGHT of previous elements, and also smaller, it
        is a candidate for being the next largest max when the window shifts.
        This point is somewhat difficult to grok unless you focus on what being
        positionally left or right means for candidate status -- noodle on this.

    The reason we have a k-sized queue is the case where you have strictly
    decreasing values within a k-group. You want the max, which will always
    be at the front, and the values stored after the front of the queue
    ALL retain their candidate status, because some later operation could
    render them the new maximum.

    Because we need access to both the front and the back for these comparisons,
    a deque is used to make sure we can pop from front and back in constant time.

    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        results = []

        i = 0
        while i < len(nums):
            # for each new element, remove all the elements in the dq
            # that are smaller than it, because these are no longer
            # relevant, back to front
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # now that we've popped the irrelevant indexes, add the
            # current index to the end for future consideration
            # (or in the case of empty dq, we have new maximum)
            dq.append(i)

            if i >= k - 1:
                # our max is always at the front of the deque for the window
                results.append(nums[dq[0]])

            # only remove the index if its actually no longer in the window
            # the item removed from the window slide could have been an
            # irrelevant smaller number not stored in our numbers-of-interest
            # queue
            if dq[0] == (i + 1) - k:
                dq.popleft()

            i += 1

        return results


def test_1():
    input = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    output = [3, 3, 5, 5, 6, 7]

    assert Solution().maxSlidingWindow(input, k) == output


def test_2():
    input = [1, 3, 1, 2, 0, 5]
    k = 3

    output = [3, 3, 2, 5]

    assert Solution().maxSlidingWindow(input, k) == output
