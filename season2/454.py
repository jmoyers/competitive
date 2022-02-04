from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # break the problem into two pairs such that
        # (a + b) + -(c + d) = 0
        # so you are looking for compliments, so you can use a hash map
        # build up a hash map of the pairs of all values
        # search for the compliment along the way
        
        pair_map = defaultdict(lambda: 0)
        ans = 0
        
        for a in nums1:
            for b in nums2:
                pair_map[a + b] += 1
        
        for c in nums3:
            for d in nums4:
                if -(c+d) in pair_map:
                    ans += pair_map[-(c+d)]
        
        return ans
        
