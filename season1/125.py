"""
---
number: 125
title: Valid Palindrome
difficulty: easy
---
Given a string, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid
palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.
"""
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        trans = str.maketrans("", "", string.whitespace + string.punctuation)
        s = s.lower().translate(trans)
        r = "".join(reversed(s))
        return s == r

    def isSlowPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start <= end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue

            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False

        return True


def test_lc1():
    inp = "A man, a plan, a canal: Panama"
    result = Solution().isPalindrome(inp)
    assert result
