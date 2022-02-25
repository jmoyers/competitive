/**
 * @param {number[]} nums
 * @return {boolean}
 */
const PredictTheWinner = (nums) => {
  const dfs = (nums, left, right, p1, p2, turn) => {
    if (left > right) {
      return p1 >= p2;
    }

    if (turn) {
      if (
        dfs(nums, left + 1, right, p1 + nums[left], p2, !turn) ||
        dfs(nums, left, right - 1, p1 + nums[right], p2, !turn)
      ) {
        return true;
      }
    } else {
      if (
        dfs(nums, left + 1, right, p1, p2 + nums[left], !turn) &&
        dfs(nums, left, right - 1, p1, p2 + nums[right], !turn)
      ) {
        return true;
      }
    }

    return false;
  };

  return (
    dfs(nums, 0, nums.length - 1, 0, 0, false) ||
    dfs(nums, 0, nums.length - 2, nums[nums.length - 1], 0, false)
  );
};
