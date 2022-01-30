from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def _canCross(self, k, distances: List[int]) -> bool:
        if (k, tuple(distances)) in self.memo:
            return self.memo[(k, tuple(distances))]

        if len(distances) == 2 and k + 1 >= distances[1] >= k - 1:
            return True

        if len(distances) == 1 and distances[0] == 0:
            return True

        options = []
        sum = 0

        for i, s in enumerate(distances[1:]):
            sum = sum + s
            if sum > k + 1:
                break
            elif k - 1 <= sum <= k + 1:
                options.append((sum, i + 2))

        for new_k, index in options:
            if self._canCross(new_k, [0] + distances[index:]):
                self.memo[(new_k, tuple([0] + distances[index:]))] = True
                self.memo[(k, tuple(distances))] = True
                return True

        self.memo[(k, tuple(distances))] = False
        return False

    def canCross(self, stones: List[int]) -> bool:
        # duh, we're allowed to skip stones
        # so this is classic backtracking problem
        # pruning options is done thru the k range

        # current k
        # the remaining stones available to us
        # current stone is assumed first in remaining stones list

        # we need to loop thru each option for next jump
        # recurse until stones is empty - this branch is true
        # we dont need the path cause its boolean return
        self.distances = [0]
        last = 0

        for s in stones[1:]:
            self.distances.append(s - last)
            last = s

        return self._canCross(0, self.distances)


def test_1():
    inp = [0, 1, 3, 5, 6, 8, 12, 17]
    assert Solution().canCross(inp)


def test_2():
    inp = [0, 1, 2, 3, 4, 8, 9, 11]
    assert not Solution().canCross(inp)


def test_3():
    inp = [0, 1, 3, 4, 5, 7, 9, 10, 12]
    assert Solution().canCross(inp)


def test_4():
    inp = [0, 2]
    assert not Solution().canCross(inp)


def test_5():
    inp = [0, 1, 3, 6, 7]
    assert not Solution().canCross(inp)


def test_6():
    inp = [0, 1, 3, 6, 10, 13, 14]
    assert Solution().canCross(inp)
