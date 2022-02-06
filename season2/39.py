from collections import defaultdict


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # permutation problem
        # the choice space (candidates) does not get smaller when branching
        # the answers are a unique set, so naively we can
        # store the answer as a sorted tuple and add it to a set so
        # no duplicates

        # express it as recursion
        # we have a path which represents the candidates chosen so far
        # ans, which a set of sorted tuples which add up to target

        ans = set()

        self.recurse(candidates, [], target, ans)

        return ans

    def recurse(self, candidates, path, target, ans):
        curr_sum = sum(path)

        if curr_sum == target:
            ans.add(tuple(sorted(path)))
            return

        allowable = [n for n in candidates if n + curr_sum <= target]

        for n in allowable:
            self.recurse(allowable, path + [n], target, ans)

