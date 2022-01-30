#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
 public:
  string fractionToDecimal(int n, int d) {
    if (n == 0 || d == 0) {
      return "0";
    }
    // convert 32 bit int to 64 bit int, so we don't overflow

    // lets check numeric limits quickly
    // on macos this stuff outputs such that int is 32, long is 64, long long
    // is 64-bit. Need to check if it compiles to 64 bit by default with
    // clang.

    // note, it does compile to 64 bit, but int is 32 bit by default

    // cout << "int max: " << numeric_limits<int>::max() << endl;
    // cout << "long max: " << numeric_limits<long>::max() << endl;
    // cout << "long long max: " << numeric_limits<long long>::max() << endl;

    // cout << "int32_t max: " << numeric_limits<int32_t>::max() << endl;
    // cout << "int64_t max: " << numeric_limits<int64_t>::max() << endl;

    int64_t num = abs(static_cast<int64_t>(n));
    int64_t den = abs(static_cast<int64_t>(d));
    int64_t whole = num / den;
    // cout << "Whole: " << whole << endl;

    int64_t remainder = num % den;
    // cout << "Remainder: " << remainder << endl;

    ostringstream ans;

    if ((n > 0 and d < 0) or (n < 0 and d > 0)) {
      ans << "-";
    }

    if (remainder == 0) {
      ans << whole;
      return ans.str();
    }


    ans << whole << ".";

    unordered_map<int64_t, int64_t> remainders;

    // store the digits in the decimal until we reach the end of the
    // remainder or until we see a repeating sequence due to a
    // repeating remainder
    vector<int> dec_digits;
    bool repeating = false;

    // loop over remainder
    while (remainder > 0) {
      if (remainders.find(remainder) != remainders.end()) {
        repeating = true;
        break;
      }

      remainders[remainder] = dec_digits.size();

      remainder *= 10;
      // cout << "rem/den: " << remainder << " / " << den << " = " << remainder / den << endl;
      // cout << "rem%den: " << remainder << " % " << den << " = " << remainder % den << endl;
      dec_digits.push_back(remainder / den);
      remainder %= den;
    }

    for (auto i = 0; i < dec_digits.size(); i++) {
      if (repeating and remainders[remainder] == i) {
        ans << "(";
      }

      ans << dec_digits[i];
    }

    if (repeating) {
      ans << ")";
    }

    return ans.str();
  }
};

int main() {
  auto ans = Solution().fractionToDecimal(INT_MIN, 1);
  cout << "Ans: " << ans << endl;
  return 0;
}
