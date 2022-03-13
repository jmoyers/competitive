/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function (nums, target) {
  nums.sort((a, b) => a - b);

  return nums.reduce((ans, n, i) => {
    if (n === target) {
      ans.push(i);
    }
    return ans;
  }, []);
};
