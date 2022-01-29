#include <unordered_map>
#include <unordered_set>
#include <set>
#include <vector>
#include <deque>
#include <string>
#include <iostream>

using namespace std;

class Solution
{
public:
  vector<vector<string>> findLadders(string beginWord, string endWord, vector<string> &wordList)
  {
    deque<vector<string>> queue;
    queue.push_back({beginWord});

    unordered_set<string> visited{beginWord};
    unordered_set<string> word_list(wordList.begin(), wordList.end());

    if (word_list.find(endWord) == word_list.end())
    {
      return vector<vector<string>>{};
    }

    vector<vector<string>> results;
    int depth = 0, found = INT_MAX;

    while (!queue.empty())
    {
      auto path = queue.front();
      auto word = path.back();

      visited.insert(word);

      if (found < path.size())
      {
        break;
      }

      if (word == endWord)
      {
        results.push_back(path);
        found = path.size();
      }

      queue.pop_front();

      for (int i = 0; i < word.length(); i++)
      {
        for (char letter = 'a'; letter <= 'z'; letter++)
        {
          string candidate = word;
          candidate[i] = letter;
          if (word_list.find(candidate) != word_list.end() and
              visited.find(candidate) == visited.end())
          {
            auto new_path = path;
            new_path.push_back(candidate);
            queue.push_back(new_path);
          }
        }
      }
    }

    return results;
  }
};

int main()
{
  string begin = "hit";
  string end = "cog";
  vector<string> word_list{"hot", "dot", "dog", "lot", "log", "cog"};
  auto results = Solution().findLadders(begin, end, word_list);
  for (auto &r : results)
  {
    cout << "path: ";
    for (auto &p : r)
    {
      cout << p << " ";
    }
    cout << endl;
  }
}