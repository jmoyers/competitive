// Given a string, find the length of the longest substring without repeating
// characters.
//
// Example 1:
//
// Input: "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
//
// Example 2:
//
// Input: "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
//
// Example 3:
//
// Input: "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.  Note that the
// answer must be a substring, "pwke" is a subsequence and not a substring.
//

const lengthOfLongestSubstring = str => {
  if (str.length === 0) return 0;

  let char_map = new OrderedHash();
  let start_index = 0;
  let end_index = 0;
  let i, j;
  i = j = 0;

  while (i < str.length && j < str.length) {
    if (char_map.get(str[j]) !== undefined) {
      let removeTo = char_map.get(str[j]);
      char_map.removeFirst(removeTo - i + 1);
      char_map.put(str[j], j);

      i = removeTo + 1;
      j++;
    } else {
      char_map.put(str[j], j);
      j++;
    }

    if (j - i > end_index - start_index) {
      start_index = i;
      end_index = j;
    }
  }

  return end_index - start_index;
};

class OrderedHash {
  constructor() {
    this.keys = {};
    this.order = [];
  }
  get(key) {
    return this.keys[key];
  }
  put(key, val) {
    this.keys[key] = val;
    this.order.push(key);
  }
  removeFirst(n) {
    let keys = this.order.splice(0, n);

    for (let k of keys) {
      delete this.keys[k];
    }
  }
}
// Input: "abcabcbb"
// Output: 3
console.log(lengthOfLongestSubstring("abcabcbb"));

// Input: "bbbbb"
// Output: 1
console.log(lengthOfLongestSubstring("bbbbb"));

// Input: "pwwkew"
// Output: 3
console.log(lengthOfLongestSubstring("pwwkew"));
