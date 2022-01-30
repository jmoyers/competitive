#include <iostream>
#include <unordered_set>
#include <set>
#include <utility>

class Solution {
 public:
  vector<pair<int, int>> twoSum(vector<int>& nums, int start, int target) {
    unordered_set<int> compliments;
    vector<pair<int, int>> ans;

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
  vector<vector<int>> threeSum(vector<int>& nums) {
    // skip dups
    sort(nums.begin(), nums.end());
    
    vector<vector<int>> ans;

    for (int i = 0; i < nums.size(); i++) {
      int comp = -nums[i];
      
      // skip dups  
      if (i == 0 or nums[i - 1] != nums[i]) {
        auto sub = twoSum(nums, i + 1, comp);
          
        for (auto &[a, b] : sub) {
          ans.push_back({nums[i], a, b});        
        }    
      }      
    }

    return ans;
  }
};

