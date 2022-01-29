"""
We are given some website visits: the user with name username[i] visited the
website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by
the time of their visits. (The websites in a 3-sequence are not necessarily
distinct.)

Find the 3-sequence visited by the largest number of users. If there is more
than one solution, return the lexicographically smallest such 3-sequence.

 

Example 1:

Input: username =
["joe","joe","joe","james","james","james","james","mary","mary","mary"],
timestamp = [1,2,3,4,5,6,7,8,9,10], website =
["home","about","career","home","cart","maps","home","home","about","career"]

Output: ["home","about","career"]

Explanation: 
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.
 

Note:

3 <= N = username.length = timestamp.length = website.length <= 50
1 <= username[i].length <= 10
0 <= timestamp[i] <= 10^9
1 <= website[i].length <= 10

Both username[i] and website[i] contain only lowercase characters.

It is guaranteed that there is at least one user who visited at least 3
websites.

No user visits two websites at the same time.
"""
from typing import List
from collections import defaultdict
from itertools import combinations


class Solution:
    """
    This question has a list of annoying gotchas. One of the worst questions
    I have encountered.

    * timestamps are not necessarily monotonically increasing
    * if a user visits the same 3-sequence more than once, its counted as 1
        because the question states "visited by the most number of users"
    * a 3-sequence is not ADJACENT visits, its the set of all permutations
        of visits by monotonically increasing timestamp
    """

    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        # keyed by user
        visits = defaultdict(list)

        # keyed by 3 tuple of websites
        sequences = defaultdict(lambda: 0)

        for user, time, site in zip(username, timestamp, website):
            visit = (site, time)
            visits[user].append(visit)

        for k in visits.keys():
            # sort by timestamp
            visits[k].sort(key=lambda x: x[1])

            # set of 3-length monotonically increasing site visits
            perms = set(combinations([rec[0] for rec in visits[k]], 3))

            for seq in perms:
                sequences[seq] += 1

        # (count, ("w1", "w2", "w3"))
        results = [(v, k) for k, v in sequences.items()]
        results.sort(reverse=True)

        final = [results[0][1]]
        max_count = results[0][0]

        # break ties with lexographic sort
        for i in range(1, len(results)):
            if results[i][0] == max_count:
                final.append(results[i][1])
            else:
                break

        final.sort()

        return list(final[0])


def test_lc1():
    usernames = [
        "joe",
        "joe",
        "joe",
        "james",
        "james",
        "james",
        "james",
        "mary",
        "mary",
        "mary",
    ]
    timestamps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    websites = [
        "home",
        "about",
        "career",
        "home",
        "cart",
        "maps",
        "home",
        "home",
        "about",
        "career",
    ]

    result = Solution().mostVisitedPattern(
        username=usernames, timestamp=timestamps, website=websites
    )

    assert result == ["home", "about", "career"]


def test_lc2():
    u = ["dowg", "dowg", "dowg"]
    t = [158931262, 562600350, 148438945]
    w = ["y", "loedo", "y"]

    results = Solution().mostVisitedPattern(u, t, w)

    assert results == ["y", "y", "loedo"]


def test_lc3():
    u = ["zkiikgv", "zkiikgv", "zkiikgv", "zkiikgv"]
    t = [436363475, 710406388, 386655081, 797150921]
    w = ["wnaaxbfhxp", "mryxsjc", "oz", "wlarkzzqht"]
    results = Solution().mostVisitedPattern(u, t, w)
    assert results == ["oz", "mryxsjc", "wlarkzzqht"]

