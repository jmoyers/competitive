#include <vector>
#include <iostream>

using namespace std;

class Solution {
  vector<int> result;
  vector<vector<int>> results;
  vector<int> nums;
public:
 void combinations(int offset, int slots) {
   if (slots == 0) {
     results.push_back(result);
     return;
   }

   // choose a letter, move forward and recurse, one less slot,
   // one less choice to choose from
   for (int i = offset; i <= nums.size() - slots; i++) {
     // choose a letter
     result.push_back(nums[i]);
     combinations(i + 1, slots - 1);
     // backtrack
     result.pop_back();
   }
 }
 vector<vector<int>> subsets(vector<int>& nums) {
   // for empty set, this copies
   results.push_back(result);
   this->nums = nums;

   for (int i = 1; i < nums.size() + 1; i++) {
     combinations(0, i);
   }

   return results;
  }
};

int main() {
  vector<int> input{1,2,3};

  auto results = Solution().subsets(input);

  for (auto& r : results) {
    for (auto& n : r) {
      cout << n << " ";
    }
    cout << "\n";
  }
}
