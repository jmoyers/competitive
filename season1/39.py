from typing import List


class Solution:
    def perms(self, target, path, allowable, solutions):
        partial = sum(path)

        allowable = [n for n in allowable if partial + n <= target]

        if partial == target:
            solutions.add(tuple(sorted(path)))
            return
        if not allowable:
            return

        for n in allowable:
            self.perms(target, path + [n], allowable, solutions)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Backtracking problem. Solve with recursion combined with a
        problem space is reduced every time you rule out a number
        by it being too large to sum to our target.
 
        Base cases:
            1. set of possible choices is 0 length
            2. or list of choices sums to target - solution
 
        target, path, allowable, solutions = []		
        """
        solution = set()
        self.perms(target, [], candidates, solution)
        return [list(a) for a in solution]
