"""
---
title: First Missing Positive
difficulty: hard
level: 3
tags:
- dictionary
- hash table
- sign flip
- in-place
links: 
- https://leetcode.com/problems/first-missing-positive
---
 Given an unsorted integer array, find the smallest missing positive integer.
 
 Example 1:
 
 Input: [1,2,0]
 Output: 3
 
 Example 2:
 
 Input: [3,4,-1,1]
 Output: 2
 
 Example 3:
 
 Input: [7,8,9,11,12]
 Output: 1
 
 Note:
 
 Your algorithm should run in O(n) time and uses constant extra space.
"""

from typing import List


class Solution:
    def firstMissingPositive2(self, nums: List[int]) -> int:
        """
        The obvious (non constant) space solution is to use a dict to map all
        the integers, and keep track of a positive minimum. Then you can
        use a range to iterate over the list from the minimum, and check the
        existance of each index in the dict

        Time: O(n)
        Space: O(n)
        """

        num_map = {}
        highest = float("-inf")

        for i, num in enumerate(nums):
            highest = num if num > 0 and num > highest else highest
            num_map[num] = i

        for i in range(1, highest + 2):
            if i not in num_map:
                return i

        return None

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        If we can guarantee the inputs are positive, we can use the sign
        of a given index in the input array as a storage mechanism as we iterate
        through the array

        So we have one loop to clean up the input (replace negative or inputs) that
        are too large with some valid benign input

        One loop to mark each seen input appropriately at their index with the
        sign flip

        One loop to check for the first position that doesn't have its sign flipped

        3n -> n
        """
        benign = len(nums) + 2

        # santize input
        for i, n in enumerate(nums):
            if n <= 0 or n > len(nums):
                nums[i] = len(nums) + 2

        for n in nums:
            if abs(n) == benign:
                continue

            # duplicates detect + sign flip
            # 1 indexed
            if nums[abs(n) - 1] > 0:
                nums[abs(n) - 1] = -nums[abs(n) - 1]

        for i, n in enumerate(nums):
            if n > 0:
                return i + 1

        return len(nums) + 1


s = Solution()
result = s.firstMissingPositive([1, 2, 0])
assert result == 3
print(result)

result = s.firstMissingPositive([3, 4, -1, 1])
assert result == 2
print(result)

result = s.firstMissingPositive([7, 8, 9, 11, 12])
assert result == 1
print(result)

result = s.firstMissingPositive([1])
assert result == 2
print(result)
