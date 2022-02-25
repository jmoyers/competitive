/**
 * @param {string} s
 * @return {number}
 */
const minimumDeletions = (s) => {
  let b = 0;
  let ans = 0;

  for (const c of s) {
    if (c === "a" && b > 0) {
      ans += 1;
      b -= 1;
    } else if (c === "b") {
      b += 1;
    }
  }

  return ans;
};
