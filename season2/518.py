class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # we can seperate this out into sub problems that build on each
        # other for an answer
        
        # if we sort the coins list and start with one coin type and
        # figure out how to make change with that coin type for every integer
        # up to amount, then we can use that data to solve for adding one more
        # coin type and so on
        
        # for instance for change(5, [1]), we solve for 0, 1, 2, 3, 4, 5 for the
        # amount using one coin type
        
        # if the amount is divisble by the coin denomination, we can make change
        # with that coin type potentially. we subtract the coin denomination from
        # the amount, and then use the remainder to check the table if we could make
        # change for the remainder
        
        # each cell in the table represents solving a subproblem. you could solve this
        # with recursion (bottom up) and an instanced memo table, but we'll solve this
        # with top down using a dp table
        
        dp = [[0 for x in range(amount + 1)] for y in range(len(coins))]
        
        coins.sort()
        
        for test_amount in range(amount + 1):
            for y, test_denom in enumerate(coins):
                # base case
                if test_amount == 0:
                    dp[y][0] = 1
                    continue
                    
                change_left = test_amount - test_denom
                combos_without_curr = dp[y-1][test_amount] if y-1 >= 0 else 0
                #print(f"test denom: {test_denom}, amount: {test_amount}")
                #print(f"change left: {change_left}, combos_without: {combos_without_curr}")
                if change_left < 0:
                    dp[y][test_amount] = combos_without_curr
                else:
                    dp[y][test_amount] = dp[y][change_left] + combos_without_curr
        
        
        return dp[len(coins)-1][amount]

def debug(dp):
    for row in dp:
        for cell in row:
            print(f'{cell} ', end="")
        print()
    print() 
