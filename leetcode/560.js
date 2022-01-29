// Given an array of integers and an integer k, you need to find the total
// number of continuous subarrays whose sum equals to k.
//
// Example 1:
//
// Input:nums = [1,1,1], k = 2
// Output: 2
//
// Constraints:
//
//     The length of the array is in range [1, 20,000].
//     The range of numbers in the array is [-1000, 1000] and the range of the
//     integer k is [-1e7, 1e7].

const subarraySum = (nums, k) => {
  const sums = {};
  let sum = 0;
  let kCount = 0;

  sums[0] = 1;

  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    if (sums[sum - k]) {
      kCount += sums[sum - k];
    }
    sums[sum] = sums[sum] !== undefined ? sums[sum] + 1 : 1;
  }

  return kCount;
};

// Input:nums = [1,1,1], k = 2
let kCount = subarraySum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0);
console.log(kCount);
