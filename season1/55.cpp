#include <algorithm>

// O(n^2)
class TopDownDP {
  unordered_map<int, bool> dp;
  
  bool _canJump(vector<int>& nums, int start) {
    if (dp.find(start) != dp.end()) {
      return dp[start];
    }
    
    int furthest = min(static_cast<int>(nums.size() - 1), start + nums[start]);
    
    for (int i = start + 1; i <= furthest; i++) {
      if (_canJump(nums, i)) {
        dp[start] = true;
        return true;
      }
    }    
    
    dp[start] = false;
    return false;
  }
public:
  bool canJump(vector<int>& nums) {
    dp[nums.size() - 1] = true;
    return _canJump(nums, 0);
  }
};

// O(n^2)
class BottomUpDP {
  enum {
    good,
    bad,
    unk
  };
  
  unordered_map<int, bool> dp;  

public:
  bool canJump(vector<int>& nums) {
    for (int i = 0; i < nums.size(); i++) {
      dp[i] = unk;
    }
    
    dp[nums.size() - 1] = good;
    
    for (int i = nums.size() - 2; i >= 0; i--) {
      int furthest = min(i + nums[i], static_cast<int>(nums.size() - 1));
      
      for (int j = i + 1; j <= furthest; j++) {
        if (dp[j] == good) {
          dp[i] = good;
          break;
        }
      }
    }
    
    return dp[0] == good;
  }
};

class Solution {
  int last_good;
  
  public:
  bool canJump(vector<int>& nums) {
    last_good = nums.size() - 1;
    
    for (int i = nums.size() - 2; i >= 0; i--) {
      if (i + nums[i] >= last_good)
        last_good = i;
    }
    
    return nums[0] >= last_good;
  }
};
