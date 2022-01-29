// There are two sorted arrays nums1 and nums2 of size m and n respectively.
//
// Find the median of the two sorted arrays. The overall run time complexity
// should be O(log (m+n)).
//
// You may assume nums1 and nums2 cannot be both empty.
//
// Example 1:
//
// nums1 = [1, 3]
// nums2 = [2]
//
// The median is 2.0
//
// Example 2:
//
// nums1 = [1, 2]
// nums2 = [3, 4]
//
// The median is (2 + 3)/2 = 2.5

const findMedianSortedArrays = (x, y) => {
  // find a partition where
  //
  // x -> x1 x2 | x3 x4 x5 x6
  // y -> y1 y2 y3 y4 y5 | y6 y7 y8
  //
  // partition of x is 2 and 4
  // parition of y is 5 and 3
  // so its 7 and 7 (even lengths on either side of the parition)
  //
  // additional properties we're looking for
  // x2 <= y6
  // y5 <= x3
  //
  // the reason is, we're looking for the 4 numbers (2 in each number set)
  // that make up the landscape surrounding the median
  //
  // so the task is to find the partition locations efficiently
  //
  // once we've found the parition then the median is
  // avg(max(x2, y5), min(x3, y6)) -- because we're essentially identifying
  // what the two numbers would be on the either side of the median if
  // we were to combine the sorted arrays via O(n) merge
  //
  // this is if the total array length is even
  //
  // for odd, it will be the max(x2, y5) because there will be an "extra"
  // element that is the exact median on the left hand side of the partition
  //
  // example
  // 1, 3, 8, 9, 15
  // 7, 11, 18, 19, 21, 25
  //
  // combined: 1, 3, 7, 8, 9, | 11, | 15, 18, 19, 21, 25
  // median: 11

  const even = (x.length + y.length) % 2 === 0;

  // one list is empty
  if (!x.length) {
    if (even) {
      return (
        (y[Math.floor(y.length / 2) - 1] + y[Math.floor(y.length / 2)]) / 2
      );
    } else {
      return y[Math.floor(y.length / 2)];
    }
  } else if (!y.length) {
    if (even) {
      return (
        (x[Math.floor(x.length / 2) - 1] + x[Math.floor(x.length / 2)]) / 2
      );
    } else {
      return x[Math.floor(x.length / 2)];
    }
  }

  const binSearch = (x, y, start, end) => {
    // perform binary search on x array where the parition is right
    // in the middle for the first iteration
    //
    // find the corresponding partion size in y array such that
    // x1 + y1 == x2 + y2 -- if its odd, 1 extra element on the left
    // paritionX + partitionY = x.length + y.length + 1 / 2
    const partitionX = start + Math.floor((end - start + 1) / 2);
    const partitionY = Math.floor((x.length + y.length + 1) / 2) - partitionX;

    // our selected partition for x is too large, we can't satisfy the
    // x1 + y1 == x2 + y2 condition, so we shrink the available partition
    // window
    if (partitionY < 0) {
      return binSearch(x, y, start, end - 1);
    }

    if (partitionY > y.length) {
      return binSearch(x, y, start + 1, end);
    }

    // Since we take the max and min for left and right respectively below,
    // if our parition creates an empty side, we use -Infinity and Infinity
    // to make sure we don't coerse undefined to 0 in Math.min/max
    const xLeft =
      x[partitionX - 1] === undefined ? -Infinity : x[partitionX - 1];
    const xRight = x[partitionX] === undefined ? Infinity : x[partitionX];
    const yLeft =
      y[partitionY - 1] === undefined ? -Infinity : y[partitionY - 1];
    const yRight = y[partitionY] === undefined ? Infinity : y[partitionY];

    // because we're parition arrays so that they have equal
    // combined lengths on left and right respectively,
    // we now test to see if the median is among the 4 numbers
    // we've isolated on either side of the paritions
    //
    // if we satisfy the condition that everything on the left side
    // of the parition of BOTH arrays is less than everything on
    // the RIGHT side of the partition of both arrays while maintaing
    // that the lengths of the the sides are equal, we've found the
    // 4 numbers that pertain to the median. once we've narrowed it down
    // to the 4, we can use min and max to find the correct pair
    //
    // if we haven't satisfied the condition that everything left is lower
    // then we need to adjust our paritions either left or right. we do
    // this via binary search partition selection and recheck our conditions
    // if we find stuff thats too big on the left, we move parition left.
    // if stuff is too small on the right, we move parition right.
    if (Math.max(xLeft, yLeft) <= Math.min(xRight, yRight)) {
      if (even) {
        return (Math.max(xLeft, yLeft) + Math.min(xRight, yRight)) / 2;
      } else {
        return Math.max(xLeft, yLeft);
      }
    } else if (xLeft > yRight) {
      return binSearch(x, y, start, partitionX - 1);
    } else {
      return binSearch(x, y, partitionX + 1, end);
    }
  };

  return binSearch(x, y, 0, x.length);
};

//let r = findMedianSortedArrays([], [2, 3]);
//let r = findMedianSortedArrays([2], []);
//let r = findMedianSortedArrays([1, 2], [3, 4]);
//let r = findMedianSortedArrays([1, 2, 3, 5, 6], [4]);
//let r = findMedianSortedArrays([3, 4], [1, 2]);
//let r = findMedianSortedArrays([1, 3], [2]);
//let r = findMedianSortedArrays([1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25]);
//let r = findMedianSortedArrays([3], [-2, -1]);
//let r = findMedianSortedArrays([1, 2, 3, 5], [4]);
let r = findMedianSortedArrays([2, 3, 4, 5, 6], [1]);

const naive = (x, y) => {
  let result = [];

  let count = 0;

  while (x.length || y.length) {
    if (x.length && y.length) {
      result.push(x[0] < y[0] ? x.shift() : y.shift());
    } else if (x.length) {
      result.push(x.shift());
    } else {
      result.push(y.shift());
    }
  }

  if (result.length % 2 == 0) {
    let partition = Math.floor(result.length / 2);
    return (result[partition - 1] + result[partition + 1]) / 2;
  } else {
    let partition = Math.floor(result.length / 2);
    return result[partition];
  }
};

console.log(r);
//console.log(naive([1, 3], [2]));

// [1, 3, 7, 8, 9, 11, 15, 18, 19, 21, 25]
//                 ^
