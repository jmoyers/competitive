#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  vector<string> reorderLogFiles(vector<string> &logs) {
    vector<pair<string, string>> dig;
    vector<pair<string, string>> let;

    for (auto log : logs) {
      auto pos = log.find(" ");

      string id = log.substr(0, pos);
      string message = log.substr(pos + 1);

      bool is_dig = true;

      for (auto c : message) {
        if (isalpha(c)) {
          is_dig = false;
        }
      }

      if (is_dig) {
        dig.push_back(make_pair(message, id));
      } else {
        let.push_back(make_pair(message, id));
      }
    }

    sort(let.begin(), let.end());

    vector<string> result;

    for (auto l : let) {
      result.push_back(l.second + " " + l.first);
    }

    for (auto d : dig) {
      result.push_back(d.second + " " + d.first);
    }

    return result;
  };
};

int main() {
  auto inp = vector<string>{"dig1 8 1 5 1", "let1 art can", "dig2 3 6",
                            "let2 own kit dig", "let3 art zero"};
  auto result = Solution().reorderLogFiles(inp);

  for (auto r : result) {
    cout << r << endl;
  }
}