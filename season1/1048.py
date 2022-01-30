from collections import Counter, defaultdict
from typing import List
from copy import copy


class Solution:
    def _dfs(self, word, count):
        if word in self.memo:
            return count + self.memo[word]

        max_chain = 0

        for a in self.adj[word]:
            max_chain = max(self._dfs(a, count + 1), max_chain)

        if not max_chain:
            return count
        else:
            self.memo[word] = max_chain - count
            return max_chain

    def longestStrChain(self, words: List[str]) -> int:
        # o n log n
        # sort the word list smallest to largest
        words.sort()

        # o n
        # dictionary of lists, where the key is the length of a given word
        lengths = defaultdict(list)
        counts = {}
        for word in words:
            counts[word] = Counter(word)
            if len(word) in lengths:
                lengths[len(word)].append(word)
            else:
                lengths[len(word)] = [word]

        # o n
        # iterate over words, smallest to largest
        # find adjacent nodes by examining the len + 1 of our length keyed dictionary
        # determine if they are indeed adjacent, add them to an adjacency list
        self.adj = defaultdict(list)
        for word in words:
            for candidate in lengths[len(word) + 1]:
                diff = 0
                w1c = copy(counts[word])
                w2c = copy(counts[candidate])

                for c, count in w1c.items():
                    if c in w2c:
                        w2c[c] -= count
                    else:
                        diff += count

                diff += sum(abs(v) for v in w2c.values())

                if diff <= 1:
                    self.adj[word].append(candidate)

        # o n
        # then do a dfs, starting at the smallest words
        # keep a hash map of word chain length to that point once we've done a dfs that
        # includes that word - this is the dynamic programming aspect to avoid duplicating traversals
        self.memo = defaultdict(lambda: 0)

        max_chain = 0
        for word in words:
            max_chain = max(self._dfs(word, 1), max_chain)

        return max_chain


def test_lc1():
    inp = ["a", "b", "ba", "bca", "bda", "bdca"]
    result = Solution().longestStrChain(inp)
    assert result == 4


def test_lc2():
    inp = [
        "sgtnz",
        "sgtz",
        "sgz",
        "ikrcyoglz",
        "ajelpkpx",
        "ajelpkpxm",
        "srqgtnz",
        "srqgotnz",
        "srgtnz",
        "ijkrcyoglz",
    ]
    result = Solution().longestStrChain(inp)
    assert result == 6


def test_lc3():
    inp = [
        "czgxmxrpx",
        "lgh",
        "bj",
        "cheheex",
        "jnzlxgh",
        "nzlgh",
        "ltxdoxc",
        "bju",
        "srxoatl",
        "bbadhiju",
        "cmpx",
        "xi",
        "ntxbzdr",
        "cheheevx",
        "bdju",
        "sra",
        "getqgxi",
        "geqxi",
        "hheex",
        "ltxdc",
        "nzlxgh",
        "pjnzlxgh",
        "e",
        "bbadhju",
        "cmxrpx",
        "gh",
        "pjnzlxghe",
        "oqlt",
        "x",
        "sarxoatl",
        "ee",
        "bbadju",
        "lxdc",
        "geqgxi",
        "oqltu",
        "heex",
        "oql",
        "eex",
        "bbdju",
        "ntxubzdr",
        "sroa",
        "cxmxrpx",
        "cmrpx",
        "ltxdoc",
        "g",
        "cgxmxrpx",
        "nlgh",
        "sroat",
        "sroatl",
        "fcheheevx",
        "gxi",
        "gqxi",
        "heheex",
    ]
    result = Solution().longestStrChain(inp)
    assert result == 9
