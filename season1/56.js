// Given a collection of intervals, merge all overlapping intervals.
//
// Example 1:
//
// Input: [[1,3],[2,6],[8,10],[15,18]]
// Output: [[1,6],[8,10],[15,18]]
// Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
// [1,6].
//
// Example 2:
//
// Input: [[1,4],[4,5]]
// Output: [[1,5]]
// Explanation: Intervals [1,4] and [4,5] are considered overlapping.
//
// NOTE: input types have been changed on April 15, 2019. Please reset to
// default code definition to get new method signature.

const merge = intervals => {
  if (intervals.length === 0) return [];

  // n * log n
  intervals.sort((a, b) => {
    return a[0] - b[0];
  });

  let start, end;
  start = intervals[0][0];
  end = intervals[0][1];

  const merged = [];

  // + n
  for (let i = 1; i < intervals.length; i++) {
    if (start <= intervals[i][0] && end >= intervals[i][0]) {
      end = Math.max(end, intervals[i][1]);
    } else {
      // new component, spit out old component and start new one
      merged.push([start, end]);
      start = intervals[i][0];
      end = intervals[i][1];
    }
  }

  // last component still there
  merged.push([start, end]);

  console.log(merged);

  return merged;
};

merge([
  [8, 10],
  [1, 3],
  [2, 6],
  [15, 18]
]);
