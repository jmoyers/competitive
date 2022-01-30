class Solution:
    def twoSum(self, nums, target):
        # we want to use a hash-based dictionary lookup table and create keys
        # for every number we encounter. that way by the end of the first
        # iteration of the numbers provided, we will be able to determine if the
        # compliment exists by checking for the existence of the key. the first
        # time we encounter a number, its likely the compliment wont be in the
        # table already, but when we encounter its compliment and we've already
        # seen the inital, it will be able to return the indexes

        # we'll store the indexes in the table as the value and the number
        # itself as the key so we can return the indexes as a pair
        lookup = {}

        for i, num in enumerate(nums):
            if (target - num) in lookup:
                return [i, lookup[target - num]]
            else:
                lookup[num] = i

        return None


def test_1():
    nums = [3, 2, 4]
    target = 6
    output = [1, 2]

    assert Solution().twoSum(nums, target), output
