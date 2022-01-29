from typing import List, Set
from collections import defaultdict


class Solution:
    def __init__(self):
        self.tmap = defaultdict(list)

    def backtrack(self, path, itinerary):
        destinations = sorted(self.tmap[path[-1]])

        if not destinations and all(len(v) == 0 for v in self.tmap.values()):
            itinerary.extend(path)
        elif not destinations:
            return

        for dest in destinations:
            self.tmap[path[-1]].remove(dest)
            self.backtrack(path + [dest], itinerary)

            if itinerary:
                return

            self.tmap[path[-1]].append(dest)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        for ticket in tickets:
            fr, to = ticket[0], ticket[1]
            self.tmap[fr].append(to)

        itinerary = []

        self.backtrack(["JFK"], itinerary)

        return itinerary


def test_lc1():
    tickets = [
        ["JFK", "SFO"],
        ["JFK", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "JFK"],
        ["ATL", "SFO"],
    ]
    result = Solution().findItinerary(tickets)
    assert result == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]


def test_lc2():
    tickets = [
        ["EZE", "AXA"],
        ["TIA", "ANU"],
        ["ANU", "JFK"],
        ["JFK", "ANU"],
        ["ANU", "EZE"],
        ["TIA", "ANU"],
        ["AXA", "TIA"],
        ["TIA", "JFK"],
        ["ANU", "TIA"],
        ["JFK", "TIA"],
    ]
    result = Solution().findItinerary(tickets)
    assert result == [
        "JFK",
        "ANU",
        "EZE",
        "AXA",
        "TIA",
        "ANU",
        "JFK",
        "TIA",
        "ANU",
        "TIA",
        "JFK",
    ]

