/**
 * @param {number[]} nums
 * @return {number}
 */
const maxSubArray = (nums) => {
  let sum = 0;
  let max = -Infinity;
  
  // iterate through all values
  // keep a running sum for the subarray up to this point
  // if the sum goes negative, we know the subarray prior to that point
  // is not useful anymore for finding the max subarray, we still compare
  // all later indexes against the max for each iteration in case this is the
  // smallest negative number we've encountered, but we can safely discard
  // the running sum from that point
  
  
  for (const n of nums) {
    sum += n;
    
    max = Math.max(max, sum);
    
    if (sum < 0) sum = 0;
  }
  
  return max;
};
