// Given an array nums of n integers where n > 1,  return an array output such
// that output[i] is equal to the product of all the elements of nums except
// nums[i].
//
// Example:
//
// Input:  [1,2,3,4]
// Output: [24,12,8,6]
//
// Constraint: It's guaranteed that the product of the elements of any prefix
// or suffix of the array (including the whole array) fits in a 32 bit integer.
//
// Note: Please solve it without division and in O(n).
//
// Follow up: Could you solve it with constant space complexity? (The output
// array does not count as extra space for the purpose of space complexity
// analysis.)
//

// 1 2 3 4
// 1 1 2 6
//
// 1 * 1
// before[0] = 1
//
// 1 *

const productExceptSelf = nums => {
  const before = [];
  const after = [];
  const result = [];

  for (let i = 0; i < nums.length; i++) {
    let a = before[i - 1] === undefined ? 1 : before[i - 1];
    let b = nums[i];

    before[i] = a * b;
  }

  for (let i = nums.length - 1; i >= 0; i--) {
    let a = after[i + 1] === undefined ? 1 : after[i + 1];
    let b = nums[i];

    after[i] = a * b;

    let x = after[i + 1] === undefined ? 1 : after[i + 1];
    let y = before[i - 1] === undefined ? 1 : before[i - 1];

    result[i] = x * y;
  }

  return result;
};

console.log(productExceptSelf([1, 2, 3, 4]));
