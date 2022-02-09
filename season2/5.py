class Solution:
    def longestPalindrome(self, s: str) -> str:
        # choose any index i
        # check expanding around i whether this is a palindrome
        # two cases
        #   1. i is the center of a palindrome, character count odd
        #   2. i is the center of a palindrome, character count even
        #   3. i is not a palindrome
        max_pal = "" 
        
        for i in range(len(s)):
            tmp = self.expand(s, i)
            if len(tmp) > len(max_pal):
                max_pal = tmp
        
        return max_pal
    
    def expand(self, s, i):
        # odd
        left, right = i, i
        
        max_left, max_right = 0, 0
        
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                if right - left > max_right - max_left:
                    max_right = right
                    max_left = left
                left -= 1 
                right += 1
            else:
                break
        
        left, right = i - 1, i
        # even
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                if right - left > max_right - max_left:
                    max_right = right
                    max_left = left
                left -= 1 
                right += 1
            else:
                break
             
        return s[max_left:max_right+1]
