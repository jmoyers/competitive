class Solution:
    def numDecodings(self, s: str) -> int:
        # this is a recursive problem that can be pruned with dp
        # example: 226
        # choice:
        #   advance pointer 1, eg 2^26
        #   advance pointer 2, eg 22^6
        # the remaining string is what is recursed on, so each stage creates two potential branches
        # so naive solution is 2^n because choices and n is input string length
        
        # because this can be expressed as a recursive tree with base cases that does repeated work
        # we can use a table to represent subproblems and calculate it linearly
        
        # each cell represents the answer to decode(up to index)
        # it can depend on the answer directly behind it (we take one character) - if non-zero, good
        # and it can depend on the answer 2 cells behind it (we take two characters) - if 1 >= num >= 27, good
        # note the linear way of looking at this is very confusing until you draw it out and try
        # to calculate it based on previous values while looking at the index you are examining
        
        # dummy value at the front because if we take two characters its valid even when index is -1
        dp = [0]*(len(s)+1)
        
        # base case
        dp[0] = 1
        dp[1] = 1
        
        if s[0] == '0':
            return 0
        
        for i in range(2, len(s)+1):
            # take one character
            if s[i-1] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i-1]
            #print('prev', dp[i-1])
            
            # take two characters, this accounts for error case where there
            # is a leading zero
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]
            
