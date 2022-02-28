/**
 * @param {number[]} nums
 * @return {string[]}
 */
const summaryRanges = (nums) => {
  if (!nums.length) return [];

  let start = nums[0],
    last = nums[0],
    ans = [];

  for (const n of nums.slice(1)) {
    if (last + 1 != n) {
      if (start !== false) {
        if (last !== start) ans.push(`${start}->${last}`);
        else ans.push(`${start}`);
      }
      start = n;
    }
    last = n;
  }

  if (start === false) ans.push(`${last}`);
  else if (last !== start) ans.push(`${start}->${last}`);
  else ans.push(`${start}`);

  return ans;
};
