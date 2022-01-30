class Solution:
    def merge(self, intervals):
        # sort the intervals by their start time, break ties with end time

        # if you were not to sort, then you'd have to loop over the entire set
        # over and over every time you examine a new interval

        # when you encounter a new interval, compare the start time to the
        # existing end time of the interval you are already examining.
        #
        # if its  start time is after the end time of the interval you have in
        # hand, add the previous interval to the output list and create a new
        # one.

        # however, if the interval that you are examining overlaps with the
        # interval you already have in hand, extend the end time of the interval
        # in hand to match the interval you are examining and continue

        # sort by start, then end, preserving
        if not intervals:
            return []

        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: (x[0], x[1]))

        existing = intervals[0]

        merged_intervals = []

        for interval in intervals[1:]:
            if existing[1] >= interval[0]:
                existing[1] = max(interval[1], existing[1])
            else:
                merged_intervals.append(existing)
                existing = interval

        merged_intervals.append(existing)

        return merged_intervals


def test_1():
    assert Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
    Solution().merge([[15, 18], [2, 6], [8, 10], [1, 3]]), [[1, 6], [8, 10], [15, 18]]
