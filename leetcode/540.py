from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        """
        Because the list is sorted, the numbers should be arranged in pairs.
        So, if you pick a value in the middle of the array, the number on
        the incorrect side should be left with length % 2 == 0

        The solo number will case the correct partition to be an odd length
        because it doesn't have a paired number. So, with binary search
        you can narrow down via the partition length.
        """

        lo, hi = 0, len(nums)

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)

            left_len, right_len = 0, 0

            if mid + 1 < len(nums) and nums[mid] == nums[mid+1]:
                left_len = mid - lo
                right_len = hi - mid - 2

                if left_len % 2 == 0:
                    lo = mid + 2
                else:
                    hi = mid - 1
            elif mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                left_len = mid - lo + 1
                right_len = hi - mid - 1

                if left_len % 2 == 0:
                    lo = mid + 1
                else:
                    hi = mid - 2
            else:
                return nums[mid]


def test_1():
    assert Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]) == 2

def test_2():
    assert Solution().singleNonDuplicate([3,3,7,7,10,11,11]) == 10

def test_3():
    assert Solution().singleNonDuplicate([1,2,2]) == 1

def test_4():
    assert Solution().singleNonDuplicate([1,1,2]) == 2

def test_5():
    assert Solution().singleNonDuplicate([1,1,2,2,4,4,5,5,9]) == 9

if __name__ == "__main__":
    test_5()
