class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # this is sort of case analysis and understanding of how permutations
        # are built
        
        # the last permutation for a given fixed root is a strictly decreasing
        # subsequence, and then it starts over with strictly increasing as the
        # first subsequence
        
        # example, 1, 2, 3, 4 is numbers, 1432 is the last subsequence before the root
        # 1 changes. this is true at any point in a permutation
        
        # such that 2431 is the last permutation for the the 2 rooted sequence
        
        # order 
        # 1234     <--
        # 1243 <-- <--
        # 1324 <--
        # 1342
        # 1423
        
        # if we search from the end until we hit a number that is smaller than previous
        # element, then we can mark that spot
        
        # given 1243, mark 2, because 4 > 2
        # prefix next permutation with 1
        # return all items larger than marked 2 to the possibility pool for next item {4, 3}
        # pick smallest {3}
        # number state is now 13__
        # now place next smallest {2} 132_
        # and next smallest {4} 1324
        
        
        # given 1234, mark 3, because 4 > 3
        # prefix next permutation with 12
        # return all items larger than 3 to the possibility pool for next {4}
        # pick new pivot {4}
        # repeat pick smallest until exhausted
        #   pick smallest {3}
        #   1243
        
        # because we have to do this in place, there is some weirdness:
        #   1. the number you need to swap with the pivot number is the first item you
        #      encounter when you reverse iterate through the right partition
        #   2. to get the first permutation with the new root you need a strictly increasing
        #      subsequence in the right partition, so you need to reverse the right part
        
        # find mark
        last = -1
        
        # 3 2 1 0 - rev index
        # 0 1 2 3 - true index
        # 1 2 3 4
        
        for i, n in enumerate(reversed(nums)):
            if n < last:
                pivot = len(nums) - i - 1
                
                # find the next largest number to swap
                for ii, nn in enumerate(reversed(nums)):
                    if nn > n:
                        to_swap = len(nums) - ii - 1
                        # print("to swap", nums[to_swap])
                        nums[pivot], nums[to_swap] = nums[to_swap], nums[pivot]
                        break
                
                # we rooted new pivot, now make it increasing subsequence so its the first
                nums[pivot+1:] = nums[pivot+1:][::-1]
                return
            last = n
       
        nums.reverse()
        
        
        
