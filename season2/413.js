/**
 * @param {number[]} nums
 * @return {number}
 */
const numberOfArithmeticSlices = (nums) => {
  if (nums.length < 3) return 0;

  // 1, 2, 3, 4, 5
  // 1, 1, 1, 1
  // x           x  - subarray length 5 (1) - n - (s - 1) --- 5 - (5 - 1) = 1
  // x     x        - subarray length 4 (2) - 5 - (4 - 1) = 2
  //    x     x
  // x  x           - subarray length 3 (3) - 5 - (3 - 1) = 3
  //    x  x
  //       x  x

  const distance = new Array(nums.length - 1);

  for (let i = 0; i < distance.length; i++) {
    distance[i] = nums[i + 1] - nums[i];
  }

  let ans = 0,
    start = 0,
    curr = distance[start];

  // 1, 2, 3, 4, 8, 12
  // 1, 1, 4, 4
  // 0, 1, 2
  //       i
  // s

  //console.log(distance);

  for (const [i, val] of distance.entries()) {
    if (val !== curr) {
      let n = i - start;

      if (n >= 2) {
        for (let j = n; j >= 2; j--) {
          ans += n - (j - 1);
        }
      }

      curr = val;
      start = i;
    }
  }

  // handle dangling
  let i = distance.length;
  let n = i - start;

  if (n >= 2) {
    for (let j = n; j >= 2; j--) {
      ans += n - (j - 1);
    }
  }

  //console.log(n, ans);

  return ans;
};
