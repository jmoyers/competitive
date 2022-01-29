"""
This problem is not all that intuitive, but you can use counting sort
and overwrite the array. This is two pass, but straightforward, I would go
for that.

Next up there is a one pass O(1) solution whereby you use 3 pointers.
leftmost 2, rightmost 0 and current index

Look at the code, swap where appropriate, have to be careful to only increment
curr index when you can guarantee that what you're swapping to can't be
in the wrong position.
"""
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, curr = 0, 0 
        p2 = len(nums) - 1
        
        while curr <= p2:
            print (nums[curr], curr, p0, p2)
            if nums[curr] == 0:                
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:                
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
            
        
