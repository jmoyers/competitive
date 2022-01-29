from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for w in strs[1:]:
            for i, c in enumerate(prefix):
                if len(w) > i:
                    if c != w[i]:
                        prefix = prefix[:i]
                        break
                else:
                    prefix = prefix[:i]
                    break
        return prefix


def test_lc1():
    inp = ["flower", "flow", "flight"]
    result = Solution().longestCommonPrefix(inp)
    assert result == "fl"
