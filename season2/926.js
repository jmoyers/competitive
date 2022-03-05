/**
 * @param {string} s
 * @return {number}
 */
var minFlipsMonoIncr = function (s) {
  // 00001000111110
  //     100012345x

  let one_count = 0,
    ans = 0;

  for (const val of s) {
    if (val === "1") {
      one_count += 1;
    } else if (val === "0") {
      if (one_count > 0) {
        ans += 1;
        one_count -= 1;
      }
    }
  }

  return ans;
};
