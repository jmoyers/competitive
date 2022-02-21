/**
 * @param {string} s
 * @return {number}
 */
const countBinarySubstrings = (s) => {
  const consec_count = [];
  let count = 0;
  let last = false;
  
  for (const c of s) {
    if (last === c || !last) {
      count += 1;
    } else {
      consec_count.push(count)
      count = 1;
    }
    last = c;
  }
  
  consec_count.push(count);
  
  //console.log(consec_count)
  
  last = consec_count[0];
  let ans = 0;
  
  for (const count of consec_count.slice(1)) {
    ans += Math.min(count, last);
    last = count;
  }
  
  return ans;
};
