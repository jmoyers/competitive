/**
 * @param {number[]} nums
 * @return {number}
 */
const deleteAndEarn = (nums) => {
  let ref = Array.from(new Set(nums));
  ref = ref.sort((a, b) => a - b);

  const memo = {};

  const points = nums.reduce((o, k) => {
    if (!o[k]) o[k] = k;
    else o[k] += k;

    return o;
  }, {});

  const dp = new Array(ref.length).fill(0);

  dp[0] = points[ref[0]];

  if (ref[1] === ref[0] + 1) {
    dp[1] = Math.max(points[ref[0]], points[ref[1]]);
  } else {
    dp[1] = points[ref[1]] + dp[0];
  }

  for (let i = 2; i < ref.length; i++) {
    if (ref[i] === ref[i - 1] + 1) {
      dp[i] = Math.max(points[ref[i]] + dp[i - 2], dp[i - 1]);
    } else {
      dp[i] = points[ref[i]] + dp[i - 1];
    }
  }

  //console.log(ref, dp);

  return dp[ref.length - 1];
};
