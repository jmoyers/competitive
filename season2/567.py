from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq, l1, l2 = Counter(s1), len(s1), len(s2)
        left, right, count = 0, 0, l1
        
        for left in range(l2):
            last = s2[left]
            first = s2[left-l1] if left >= l1 else ''
            
            if first in freq:
                freq[first] += 1
            
            #print(first, last, freq)
            
            if last in freq:
                freq[last] -= 1
                
                if all(val == 0 for val in freq.values()):
                    return True
        
        return False
            
        
        
