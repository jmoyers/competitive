#include <iostream>
#include <unordered_set>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
 public:
  vector<vector<int>> twoSum(vector<int>& nums, int target, int start) {
    unordered_set<int> compliments;
    vector<vector<int>> ans;

    for (int i = start; i < nums.size(); i++) {
      int comp = target - nums[i];
      if (compliments.find(comp) != compliments.end()) {
        ans.push_back({comp, nums[i]});
        
        // skip dups
        while (i + 1 < nums.size() and nums[i] == nums[i + 1]) {
          i++;  
        }          
      }
      compliments.insert(nums[i]);      
    }

    return ans;
  }
  vector<vector<int>> kSum(vector<int> &nums, int target, int start, int k) {
    // lets model this with recursion
    //
    // every time we loop, we subtract 1 from k and add one to the result
    //
    // we also need to change the target, because its now the compliment -
    // the newly selected element for k - 1 sum
    //
    // vector. the base case is twoSum, which uses hash table compliment O(n)
    // so we should have O(n^(k-1)) run time
    vector<vector<int>> ans;

    // base case, we can't hit the target
    if (start == nums.size() or 
        nums[start] * k > target or
        target > nums.back() * k) {
      return ans;
    }

    // base case, we can hit the target, check twosum
    if (k == 2) {
      return twoSum(nums, target, start);
    }

    for (int i = start; i < nums.size(); i++) {
      // skip dups
      if (i == start or nums[i - 1] != nums[i]) {
        for (auto &sub : kSum(nums, target - nums[i], i + 1, k - 1)) {
          // we know that at least nums[i] is in the answer, then we copy
          // the result of the sub_result into the back of the answer, since
          // we want this to be generic for k, we use the start/end of the 
          // sub_result
          ans.push_back({nums[i]});
          ans.back().insert(ans.back().end(), sub.begin(), sub.end());
        }
      }
    }

    return ans;
  }
  vector<vector<int>> fourSum(vector<int>& nums, int target) {
    // skip dups
    sort(nums.begin(), nums.end());
    return kSum(nums, target, 0, 4);
  }
};

int main() {
  vector<int> inp = {1,0,-1,0,-2,2};
  auto r = Solution().fourSum(inp, 0);

  cout << "ans: " << endl;
  for (auto& l : r) {
    for (auto& n : l)
      cout << n << " ";
    cout << endl;
  }
}
