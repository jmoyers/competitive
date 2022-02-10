from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # create a cummulative sum array 
        # use the cummulative sum array to determine the sum
        # between two elements by subtraction
        
        sum_array = [0] * len(nums)
        sums = defaultdict(list)
        
        for i in range(len(nums)):
            sum_array[i] = (sum_array[i-1] if i - 1 >= 0 else 0) + nums[i]
            sums[sum_array[i]].append(i)
        
        ans = 0
        
        #print(sum_array, sums)
        
        for right in range(len(nums)):
            compliment = sum_array[right] - k
            #print('compliment', compliment, sum_array[right], k, sums[compliment])
            
            if compliment == 0:
                #print('right on')
                ans += 1
                
            for left in sums[compliment]:
                if left < right:
                    #print('found comp')
                    ans += 1
                    
        return ans
