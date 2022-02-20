/**
 * @param {string} s
 * @return {string}
 */
const longestPalindrome = (s) => {
  // for each index i, we can grow around that point
  // two cases -- one is the ith character is the actual center of a palindrome
  // even letter case -- letters on either side of the index are the same and we grow from there
  if (!s.length) return 0;
  
  let max = 1;
  let ans = {start: 0, length: 1};
  
  for (let i = 0; i < s.length; i++) {
    //console.log('center', s[i]);
    // ith letter is the center
    let count = 1, j = 1;
    
    while (i-j >= 0 && i+j < s.length) {
      //console.log(s[i-j], s[i+j])
      if (s[i-j] == s[i+j]) {
        count += 2;
        if (count > max) {
          max = count;
          ans.start = i - j;
          ans.length = (i + j + 1) - (i - j);
          //console.log('new max', ans)
        }
        j += 1;
      } else {
        //console.log('first case dead')
        break;
      }
    }
    
    // on either side of i
    count = 0, j = 1;
    
    while (i-j >= 0 && (j+i-1) < s.length) {
      //console.log(s[i-j], s[i+j-1])
      if (s[i-j] == s[i+j-1]) {
        count += 2;
        if (count > max) {
          max = count;
          ans.start = i - j;
          ans.length = (i + j) - (i - j);
          //console.log('new max', ans)
        }
        j += 1;
      } else {
        //console.log('second case dead')
        break;
      }
    }
  }
  
  return s.substr(ans.start, ans.length);
};
