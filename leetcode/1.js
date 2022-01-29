// Given an array of integers, return indices of the two numbers such that they
// add up to a specific target.
//
// You may assume that each input would have exactly one solution, and you may
// not use the same element twice.
//
// Example:
//
// Given nums = [2, 7, 11, 15], target = 9,
//
// Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
//

const twoSum = (nums, target) => {
  // Use a map to quickly find compliments via O(1) lookup
  // O(n) to create the map

  const lookup = {};

  for (let i = 0; i < nums.length; i++) {
    const n = nums[i];
    const compliment = target - n;

    console.log("n", n, "compliment", compliment, lookup);

    if (lookup[compliment] !== undefined) {
      return [i, lookup[compliment]];
    }

    lookup[n] = i;
  }

  return false;
};

console.log(twoSum([2, 7, 11, 15], 9));
