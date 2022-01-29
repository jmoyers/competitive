from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshhold: int) -> int:
        """
        We binary search. The range is the 0 to the max of the values
        given to us in nums. The we loop thru the array given that
        divisor and try to see if its close to threshhold.
        """

        # right side is the max value inside nums array, because if we
        # divide by that number, the sum can't get any smaller (1 for
        # each value inside the array
        l, r = 1, max(nums)

        while l < r:
            # integer division
            divisor = (l + r) // 2

            # note question specifically says this is rounded up,
            # not integer division
            test_sum = sum(math.ceil(n / divisor) for n in nums)

            if test_sum > threshhold:
                l = divisor + 1
            else:
                r = divisor

        # we want the soluion that is closest to thresshold
        # also, l is a divisor, not search for some value in the array
        return l


def test_1():
    ans = Solution().smallestDivisor([1,2,5,9], 6);
    assert ans == 5

if __name__ == '__main__':
    test_1()
