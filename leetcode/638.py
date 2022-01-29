"""
---
number: 636
title: Exclusive Time of Functions
difficulty: medium
tags:
- interval
- recursion
---

On a single threaded CPU, we execute some functions.  Each function has a unique id between 0 and N-1.

We store logs in timestamp order that describe when a function is entered or exited.

Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".  For example, "0:start:3" means the function with id 0 started at the beginning of timestamp 3.  "1:end:2" means the function with id 1 ended at the end of timestamp 2.

A function's exclusive time is the number of units of time spent in this function.  Note that this does not include any recursive calls to child functions.

The CPU is single threaded which means that only one function is being executed at a given time unit.

Return the exclusive time of each function, sorted by their function id.

 

Example 1:



Input:
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3, 4]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 units of time and reaches the end of time 1.
Now function 1 starts at the beginning of time 2, executes 4 units of time and ends at time 5.
Function 0 is running again at the beginning of time 6, and also ends at the end of time 6, thus executing for 1 unit of time. 
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
 

Note:

1 <= n <= 100
Two functions won't start or end at the same time.
Functions will always log when they exit.
"""
from typing import List
from collections import deque, defaultdict


class Solution:
    """
    I had a hard time understanding all the cases at first. Recursive functions
    "not counting" was a big red herring that I tried to code for, but it ended
    up not meaning exactly what I thought it did. Recursive functions count in
    their occupancy of the cpu, but not against the parents run time. On the
    other hand you don't actually need to keep track of recursion in the stack
    based method I used, because I'm also keeping track of the "penalty" a
    function receives if another function runs over the top of it, so we end up
    subtracting the runtime of the child recursive call from the parent anyway.
    This method is a little slow, and I think there is a little trick where you
    only have to add a penalty to the next item in the stack, because in essence
    it passes its penalty down the stack via the way the algorithm works, but i
    would have had to reorganize things to make that work and this passes.
    """

    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if n == 0:
            return 0

        events = deque([])

        for log in logs:
            parsed = log.split(":")
            id, type, timestamp = int(parsed[0]), parsed[1], int(parsed[2])
            events.append((timestamp, type, id))

        results = [0] * n

        waiting = []
        starts = defaultdict(list)

        while events:
            timestamp, type, id = events.popleft()

            if type == "start":
                waiting.append([id, 0])
                starts[id].append(timestamp)

            if type == "end":
                rec = waiting.pop()
                start = starts[id].pop()
                duration = (timestamp - start + 1) - rec[1]

                for wait in waiting:
                    wait[1] += duration

                results[id] += duration

        return results


def test_lc1():
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    assert Solution().exclusiveTime(2, logs) == [3, 4]


def test_lc2():
    result = Solution().exclusiveTime(
        3,
        [
            "0:start:0",
            "0:end:0",
            "1:start:1",
            "1:end:1",
            "2:start:2",
            "2:end:2",
            "2:start:3",
            "2:end:3",
        ],
    )
    assert result == [1, 1, 2]


def test_lc3():
    n = 8
    logs = [
        "0:start:0",
        "1:start:5",
        "2:start:6",
        "3:start:9",
        "4:start:11",
        "5:start:12",
        "6:start:14",
        "7:start:15",
        "1:start:24",
        "1:end:29",
        "7:end:34",
        "6:end:37",
        "5:end:39",
        "4:end:40",
        "3:end:45",
        "0:start:49",
        "0:end:54",
        "5:start:55",
        "5:end:59",
        "4:start:63",
        "4:end:66",
        "2:start:69",
        "2:end:70",
        "2:start:74",
        "6:start:78",
        "0:start:79",
        "0:end:80",
        "6:end:85",
        "1:start:89",
        "1:end:93",
        "2:end:96",
        "2:end:100",
        "1:end:102",
        "2:start:105",
        "2:end:109",
        "0:end:114",
    ]

    result = Solution().exclusiveTime(n, logs)
    assert result == [20, 14, 35, 7, 6, 9, 10, 14]

