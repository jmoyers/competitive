"""
---
title: Most Common Words
number: 819
difficulty: easy
tags:
- frequency counter
- hash map
- set
- parsing
- string
links:
- https://leetcode.com/problems/most-common-word/
---
Given a paragraph and a list of banned words, return the most frequent word
that is not in the list of banned words. It is guaranteed there is at least
one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of
punctuation. Words in the paragraph are not case sensitive. The answer is in
lowercase.

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 

"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent
non-banned word in the paragraph.

Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
 

Note:

1 <= paragraph.length <= 1000.
0 <= banned.length <= 100.
1 <= banned[i].length <= 10.
The answer is unique, and written in lowercase (even if its occurrences in
paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.

There are no hyphens or hyphenated words.

Words only consist of letters, never apostrophes or other punctuation symbols.
"""
from typing import List
from collections import Counter
from string import punctuation


class Solution:
    def mostCommonWord(self, p: str, banned: List[str]) -> str:
        banned = set(banned)

        # lowecase it
        p = p.lower()

        # get rid of punctation
        p = p.translate(str.maketrans({k: " " for k in punctuation}))

        if p == "":
            return ""

        word_list = p.split(" ")

        if len(word_list) == 0:
            return ""

        counts = Counter(word_list)

        if "" in counts:
            del counts[""]

        counts = [(cnt, word) for word, cnt in counts.items()]
        counts.sort()

        candidate = counts.pop()
        while candidate[1] in banned:
            candidate = counts.pop()

        if candidate[1] in banned:
            return ""
        else:
            return candidate[1]


def test_lc1():
    p = "a, a, a, a, b,b,b,c, c"
    ban = ["a"]

    result = Solution().mostCommonWord(p, ban)
    assert "b" == result
