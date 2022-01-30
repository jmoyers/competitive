"""
Fairly classic O(n) two pointer solution because condition is "contiguous," which can be nicely tracked by a slow and fast pointer and guarantees we only examine each element at most 2 (+/-) time.
"""

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        min_contig, slow, fast = len(nums) + 1, 0, 0

        slice_sum = nums[0]

        """
        Input: s = 7, nums = [2,3,1,2,4,3]
        Output: 2
        """

        while fast < len(nums) and slow <= fast:
            if slice_sum >= s:
                min_contig = min(min_contig, fast - slow + 1)
                slow += 1
                if slow - 1 >= 0:
                    slice_sum -= nums[slow - 1]
            else:
                fast += 1
                if fast < len(nums):
                    slice_sum += nums[fast]

        return min_contig if min_contig != len(nums) + 1 else 0


def test_lc1():
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    result = Solution().minSubArrayLen(s, nums)
    assert result == 2
