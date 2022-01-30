#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

class Solution {
  public:
    int threeSumClosest(vector<int>& nums, int target) {
      // one outer loop
      // fix the first number in the triplet based on outer loop index
      // other two indexes start lo = i+1, hi = nums.size() - 1
      // while lo < hi
      //  check if i + lo + hi
      //    > decrease hi
      //    < increase lo
      //    == return
      //
      //    each iteration store the min the difference to target with
      //    min_diff
      //
      
      sort(nums.begin(), nums.end());

      int min_diff = INT_MAX, min_sum = INT_MAX;

      for (int i = 0; i < nums.size(); i++) {
        int lo = i + 1, hi = nums.size() - 1;

        while (lo < hi) {
          int candidate = nums[i] + nums[lo] + nums[hi];
          int diff = abs(target - candidate);

          if (min_diff > diff) {
            min_diff = diff;
            min_sum = candidate;
          };
          
          if (candidate > target) {
            hi--;
          } else if (candidate < target) {
            lo++;
          } else {
            return candidate;
          }
        }
      }

      return min_sum;
    }
};

