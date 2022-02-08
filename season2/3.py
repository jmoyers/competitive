class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        # character map to count freqeuncty for a given range
        # when we hit a repeating character, we move the left pointer
        # forward to the given character instance
        
        chars = {}
        
        left = 0
        
        max_substring = -math.inf
        
        for right, c in enumerate(s):
            if c in chars:
                new_left = chars[c] + 1
                for remove_c in s[left:new_left]:
                    chars.pop(remove_c, None)
                left = new_left
                
            chars[c] = right
            #print(s[left:right+1], max_substring, right-left+1)
            max_substring = max(max_substring, right - left+1)
        
        return max_substring
                
            
