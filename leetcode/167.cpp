#include <iostream>
#include <vector>

class Solution {
  public:
    vector<int> twoSum(vector<int>& nums, int target) {
    // since these items are sorted, we can use that for a two pointer approach
    // to solve in o n

    int lo = 0, hi = nums.size() - 1;

    while (lo < hi) {
      int a = nums[lo], b = nums[hi];
      int candidate = a + b;
      // if smaller increase lo, if larger decrease hi
      // this is dependent on only one answer being required
      if (candidate == target) {
        return {lo+1, hi+1};
      } else if (candidate < target) {
        lo++;
      } else {
        hi--;
      }
    }
    return {0,0};
  }
};
