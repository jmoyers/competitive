class Solution {  
  void is_palindrome(string s, int left, int right, int& ans) {
    while (left >= 0 and right <= s.size() and s[left] == s[right]) {
      ans++;
      left--;
      right++;
    }
  }
public:
  int countSubstrings(string s) {
    // treat each index as the center of a palindrome.
    // expand the palindrome, counting new palindromes, stop when we reach the first invalid palindrome
    
    int ans = 0;
    
    for (int i = 0; i < s.size(); i++) {
      is_palindrome(s, i, i, ans);    // odd length
      is_palindrome(s, i, i+1, ans);  // even length palindromes, where i is the left of center index
    }
    
    return ans;
  }
};
