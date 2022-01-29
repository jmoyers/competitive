"""
---
title: Search in Rotated Sorted Array
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/search-in-rotated-sorted-array
---
Suppose an array sorted in ascending order is rotated at some pivot unknown
to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its
index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1:
            return -1

        # you can find the partion in log n time with a binary search
        # once we find the pivot, you can choose which parition to search
        # for the needle in and binary search there

        start, end = 0, len(nums)
        partition = -1

        while partition == -1 and start < len(nums):
            # select an index half way between start and end
            index = start + (end - start) // 2

            if target == nums[index]:
                return index
            if nums[0] > nums[index] and nums[index] < nums[index - 1]:
                partition = index
            elif nums[0] > nums[index]:
                # check left
                end = index - 1
            else:
                # check right
                start = index + 1

        if partition == -1:
            start, end = 0, len(nums)
        elif nums[0] > target:
            start = partition + 1
            end = len(nums)
        else:
            start = 0
            end = partition - 1

        while start <= end and start < len(nums):
            index = start + (end - start) // 2

            if target == nums[index]:
                return index
            elif nums[index] > target:
                end = index - 1
            else:
                start = index + 1

        return -1


# result = Solution().search([4,5,6,7,0,1,2], 0)
# print(result)
# assert(result == 4)
#
# result = Solution().search([4,5,6,7,0,1,2], 3)
# print(result)
# assert(result == -1)
#
# result = Solution().search([5,6,7,8,9,10,11,12,13,1,3,4], 3)
# print(result)
# assert(result == 10)

# result = Solution().search([], 3)
# print(result)
# assert(result == -1)
#
# result = Solution().search([3], 3)
# print(result)
# assert(result == 0)

# result = Solution().search([3], 0)
# print(result)
# assert(result == -1)
#
# result = Solution().search([3, 2], 0)
# print(result)
# assert(result == -1)

# result = Solution().search([2, 3], 0)
# print(result)
# assert(result == -1)
#
# result = Solution().search([2, 3], 3)
# print(result)
# assert(result == -1)
result = Solution().search([1, 3], 1)
print(result)
assert result == 0
