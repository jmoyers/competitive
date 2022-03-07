/**
 * @param {number[]} nums
 * @return {number}
 */
const minDifference = (nums) => {
  if (nums.length < 4) return 0;

  nums = nums.sort((a, b) => a - b);

  // our end array should have 3 less elements. test via sliding window!

  let min = Infinity,
    start = 0,
    end = nums.length - 4; // 3 extra so the window matches end window!

  //console.log(nums);

  for (let i = 0; i < 4; i++) {
    //console.log('test', nums[end+i], nums[start+i]);
    min = Math.min(nums[end + i] - nums[start + i], min);
  }

  return min;
};
