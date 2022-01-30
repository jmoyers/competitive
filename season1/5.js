// Given a string s, find the longest palindromic substring in s. You may
// assume that the maximum length of s is 1000.
//
// Example 1:
//
// Input: "babad"
// Output: "bab"
// Note: "aba" is also a valid answer.
//
// Example 2:
//
// Input: "cbbd"
// Output: "bb"
//
const longestPalindrome = s => {
  let index = 0;
  let length = 0;

  for (let i = 0; i < s.length; i++) {
    let candidate1 = expandFromMiddle(s, i, i); // racecar
    let candidate2 = expandFromMiddle(s, i, i + 1); // abba

    const candidate = Math.max(candidate1, candidate2);

    if (candidate > length) {
      length = candidate;
      index = i - Math.ceil(length / 2) + 1;
    }
  }

  return s.slice(index, index + length);
};

// returns the size of substring from a given point if
// it is a palindrome
//
// ex:
// in this case left and right are 1 apart
// a b b a - 4
//    ^
// in this case left and right are == at the start
// r a c e c a r - 7
//       ^
const expandFromMiddle = (s, left, right) => {
  while (left >= 0 && right < s.length && s[left] === s[right]) {
    left--;
    right++;
  }

  // we've decremented and incremented one too far (2 len, and its 0 indexed)
  // so we - 1
  return right - left - 1;
};

console.log(longestPalindrome("racecar"));
console.log(longestPalindrome("cbbd"));
