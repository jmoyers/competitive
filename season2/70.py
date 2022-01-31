 class Solution:
    def climbStairs(self, n: int) -> int:
        # this seems like it can be split into subproblems, so it suggests dynamic programming
        # the sub problems climbStairs(n) = climbStairs(n-2) + climbStairs(n-1)
        # if we take a bottom up apporoach we could recursively solve climbStairs and
        # store the results for n in a memo table and use the memo table when we repeat work
        # other branches of the tree. if we don't memoize its O 2^n because there are two
        # choices to express at every recursion. if we memoize, its somewhat less!
        
        # we'll express this via top down, which we'll use a 1d table for, and we'll start with
        # 0 steps and move up to n steps building the answer as we go
        
        dp = [1] * (n+1)
        
        for numSteps in range(2, n+1):
            s1 = dp[numSteps - 1] if numSteps - 1 >= 0 else 1
            s2 = dp[numSteps - 2] if numSteps - 2 >= 0 else 1
            dp[numSteps] = s1 + s2
        
        return dp[n]eason2
