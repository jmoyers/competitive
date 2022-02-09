class Solution:
    def trap(self, heights: List[int]) -> int:
        # at each i, check the left and right max to see if its higher than
        # the current point. if it is, this index can trap water
        # this is a bit of a dynamic programming problem because the left/right
        # max can be calculated based on the left/right max of the previous index
        
        left_max = [0] * len(heights)
        right_max = [0] * len(heights)
        
        
        for rev_i, height in enumerate(reversed(heights)):
            i = len(heights) - rev_i - 1
            right_max[i] = max(right_max[i+1] if i + 1 < len(heights) else 0, height)
        
        trapped = 0
            
        for i, height in enumerate(heights):
            #print(i, height, left_max[i-1] if i - 1 >= 0 else 0)
            left_max[i] = max(left_max[i-1] if i - 1 >= 0 else 0, height)
            
            if height < max(left_max[i], right_max[i]):
                trapped += min(left_max[i], right_max[i]) - height
        
        #print(left_max, right_max)
        
        return trapped
        

