// Given n non-negative integers representing an elevation map where the width
// of each bar is 1, compute how much water it is able to trap after raining.
//
// Example:
//
// Input: [0,1,0,2,1,0,1,3,2,1,2,1]
// Output: 6

const trap = heights => {
  let left_max = new Array(heights.length);
  let right_max = new Array(heights.length);
  let water = 0;
  // to avoid calculating the left and right max separately for each index
  // we need to store the result of previous examinations and then compare
  // it iteratively to the current index. because its a maximum, it follows
  // that the next index can use the results of examining all the previous
  // indexes for local maximums

  // we seed the first index with the height as the first maximum, because
  // the edges of the array are "emtpy" and therefor contain no maximum to
  // compare to
  left_max[0] = heights[0];

  // start at 1, as 0 is seeded
  for (let i = 1; i < heights.length; i++) {
    // calculate each indexes left_max based on the left_max of the previous
    // index. we compare it to the height of the current index in case we
    // find a new maximum at our current index
    left_max[i] = Math.max(heights[i], left_max[i - 1]);
  }

  // similar to left we have to seed the right
  right_max[heights.length - 1] = heights[heights.length - 1];

  // this has to go right to left here, as our optimization depends on using
  // data from the edges of the array inwards due to the nature of the
  // problem (e.g. water is trapped by creating a cavity)
  for (let i = heights.length - 2; i >= 0; i--) {
    right_max[i] = Math.max(heights[i], right_max[i + 1]);
  }

  // lastly loop through each index and find the minimum of the local maximums
  // for both left and right to find the "ceiling" for the water trapped
  // at each index
  for (let i = 0; i < heights.length; i++) {
    water += Math.min(left_max[i], right_max[i]) - heights[i];
  }

  return water;
};

console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]));
