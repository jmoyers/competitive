/**
 * @param {string[]} strs
 * @return {string[][]}
 */
const groupAnagrams = (words) => {
  const groups = {};
  
  for (const w of words) {
    const freq = {}
    
    for (const c of w) {
      freq[c] = freq[c] ? freq[c] + 1 : 1;
    }
    
    const key = Object.keys(freq).sort().reduce((gen, k) => {
      gen += ","+ k + "=" + freq[k];
      return gen;
    }, "");
    
    if (groups[key]) {
      groups[key].push(w);
    } else {
      groups[key] = [w];
    }
  }
  
  return Object.keys(groups).map((k) => groups[k]);
};
