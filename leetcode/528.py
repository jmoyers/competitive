"""
---
title: Random Pick with Weight
number: 528
difficulty: medium
tags:
- random
- array
- bisect
- binary search
- accumulate
links:
- https://stackoverflow.com/questions/1761626/weighted-random-numbers
- https://leetcode.com/problems/random-pick-with-weight/
---

Given an array w of positive integers, where w[i] describes the weight of index i(0-indexed), write a function pickIndex which randomly picks an index in proportion to its weight.

For example, given an input list of values w = [2, 8], when we pick up a number out of it, the chance is that 8 times out of 10 we should pick the number 1 as the answer since it's the second element of the array (w[1] = 8).
 

Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. 

Since there is only one single element on the array the only option is to
return the first element.

Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. 
// It's returning the second element (index = 1) that has probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. 
// It's returning the first element (index =  0) that has probability of 1/4.

Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
 

Constraints:

    1 <= w.length <= 10000
    1 <= w[i] <= 10^5
    pickIndex will be called at most 10000 times.
"""

from random import randrange
from functools import reduce
from itertools import accumulate
from collections import Counter
from typing import List
import bisect


class Solution:
    """
    Sum the array we're given.

    Choose a random number between 0 and the sum.

    Iterate through the weight list, subtracting the weight from your random
    number. If you find the weight is bigger than the number you have, this
    is the number we've picked.

    If we have more than a dozen numbers in list, you can use a binary search
    to find the target weight.

    The key to the binary search is essentially keeping a running total
    of the weights at each index. this will keep them monotonically
    increasing, which makes it valid for a binary search as well as being
    analagous to the subtraction based algorithm.
    """

    def __init__(self, w: List[int]):
        self.weights = list(accumulate(w))
        self.sum = reduce(lambda a, b: a + b, self.weights)

    def pickIndex(self) -> int:
        value = randrange(0, self.weights[-1])

        i = bisect.bisect_right(self.weights, value)
        return i


def test_lc1():
    """
    ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
    [[[1,3]],[],[],[],[],[]]
    Output
    [null,1,1,1,1,0]
    """
    r = Solution([1, 3])

    results = []
    for _ in range(10000):
        results.append(r.pickIndex())

    results = Counter(results)
    print(results)


test_lc1()
