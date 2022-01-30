from collections import deque


class Solution:
    """
    Typically when we're looking for the shortest path, we're
    going to choose a breadth first search-based algorithm,
    if our goal is not to traverse the entire graph.
 
    With an infinite board, we don't want to traverse the entire
    graph.
 
    However, this is a special case, as the board can get quite
    large and we could do a ton of unnecessary work if we didn't
    prune the edge selection at a given node.
 
    I would split this into two problems -- one is to drive at
    the target node directly until we reach some distance n, and
    then start looking for a shortest path from there. The
    reason I think we shoot in more or less a straight line
    early on, is that this is going to greatly prune the bfs
    and is sort of self-evidently obviously the solution. You
    would never start an optimal traversal of this type of graph
    by going the opposite direction, or indeed even any of the
    other 7/8 possibilities that are not the most direct general
    direction towards your target point.
 
    I'm not sure what the n distance is, but I bet we prove this
    through experimentation. Basically select a value n, and 
    decrement it until we start to get an incorrect solution
    for a known optimally solved test case.
    """

    def minKnightMoves(self, x: int, y: int) -> int:
        # first lets move x and y to a much closer
        # location (within say 5 units) based on the
        # most direct route. moving the target itself
        # is kind of a brain bending way of doing this
        # but there ends up being less bookkeeping, i think

        # we also don't care if x and y are negative, since
        # we aren't looking for an actual list of moves,
        # we're looking for the length of the shortest path
        x, y, move = abs(x), abs(y), 0

        while x > 5 or y > 5:
            move += 1

            if x > y - 2 and y > 0:
                x -= 2
                y -= 1
            elif x > y - 2:
                x -= 2
                y += 1
            elif y > x - 2 and x > 0:
                y -= 2
                x -= 1
            else:
                y -= 2
                x += 1

        # here the target should be within 5
        # start a bfs
        # y, x, distance so far
        # root is origin
        queue = deque([(0, 0, 0)])

        moves = ((1, -2), (2, -1), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1))

        while queue:
            y1, x1, dist = queue.popleft()
            if y1 == y and x1 == x:
                return dist

            # explore the children
            for dy, dx in moves:
                # could perform some branch optimization
                # here by pruning moves that go away
                next_y = y1 + dy
                next_x = x1 + dx

                if (next_y, next_x) == (y, x):
                    return dist + 1 + move
                elif y - next_y < y - y1 or x - next_x < x - x1:
                    queue.append((next_y, next_x, dist + 1))


def test_lc1():
    assert Solution().minKnightMoves(2, 1) == 1


def test_lc2():
    assert Solution().minKnightMoves(5, 5) == 4


def test_lc3():
    assert Solution().minKnightMoves(130, -86) == 72
