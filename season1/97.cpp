#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
  enum Memo { unk, bad, good };
  vector<vector<Memo>> memo;
  string s1, s2, s3;

 public:
  bool isInterleave(string _s1, string _s2, string _s3) {
    if (_s1.size() + _s2.size() != _s3.size()) return false;
    if (_s1.empty() and _s2.empty() and _s3.empty()) return true;

    s1 = move(_s1);
    s2 = move(_s2);
    s3 = move(_s3);

    memo = vector<vector<Memo>>(s1.size(), vector<Memo>(s2.size(), unk));

    return _isInterleave(0, 0, 0);
  }

  bool _isInterleave(int p1, int p2, int p3) {
    if (p1 == s1.size()) {
      return s2.substr(p2) == s3.substr(p3);
    }

    if (p2 == s2.size()) {
      return s1.substr(p1) == s3.substr(p3);
    }

    if (memo[p1][p2] == bad) {
      return false;
    }

    if (s1[p1] == s3[p3] and _isInterleave(p1 + 1, p2, p3 + 1)) {
      return true;
    }

    if (s2[p2] == s3[p3] and _isInterleave(p1, p2 + 1, p3 + 1)) {
      return true;
    }

    memo[p1][p2] = bad;
    return false;
  }
};

int main() {
  bool ans = Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac");
  cout << (ans ? "true" : "false") << endl;
}
