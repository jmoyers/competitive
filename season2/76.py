from collections import Counter, defaultdict
import math

class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        min_window = ""
        start = 0
        remaining = len(t)
        counts = Counter(t)
        
        # check all end positions
        for end in range(len(s)):
            char = s[end]
            
            if char in counts:
                if counts[char] > 0:
                    # we still need this letter
                    remaining -= 1
                counts[char] -= 1
                
            while remaining == 0:
                # increment start until its not valid
                
                char = s[start]
                
                if not min_window or len(min_window) > end - start:
                    min_window = s[start:end+1]
                
                if char in counts:
                    counts[char] += 1
                    if counts[char] > 0:
                        remaining += 1
                
                start += 1 
                
        return min_window
        
                    
