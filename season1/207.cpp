#include <chrono>
#include <vector>
#include <unordered_set>
#include <iostream>

using namespace std::chrono;
using namespace std;

class VecSolution {  
  vector<bool> visited;
  vector<vector<int>> adj;
  decltype(std::chrono::high_resolution_clock::now()) s;
  decltype(std::chrono::high_resolution_clock::now()) e;      
  
  bool dfs(int node, unordered_set<int>& path) {    
    visited[node] = true;
    s = chrono::high_resolution_clock::now();      
    path.insert(node);
    e = chrono::high_resolution_clock::now();
    cout << "Insert: " << duration_cast<nanoseconds>(e - s).count() << endl;      

    for (auto &neighbor : adj[node]) {
      s = chrono::high_resolution_clock::now();      
      if (path.find(neighbor) != path.end()) {
        return true;
      }      
      e = chrono::high_resolution_clock::now();
      cout << "Find: " << duration_cast<nanoseconds>(e - s).count() << endl;      

      if (visited[neighbor]) {
        continue;
      }
      
      s = chrono::high_resolution_clock::now();
      auto path_branch = path;
      e = chrono::high_resolution_clock::now();
      cout << "Copy: " << duration_cast<nanoseconds>(e - s).count() << endl;

      if (dfs(neighbor, path_branch)) {
        return true;
      }
    }

    return false;
  }
public:
  bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
    // basically we need to make sure there are no dependency cycles between
    // classes. we can do dfs cycle detection or we can try to
    // do a topological sort

    visited = vector<bool>(numCourses);
    adj = vector<vector<int>>(numCourses, vector<int>());

    for (auto &p : prerequisites) {
      adj[p[0]].push_back(p[1]);
    }
    
    for (int i = 0; i < numCourses; i++) {
      if (!visited[i]) {
        auto path = unordered_set<int>();
        if (dfs(i, path)) {
          return false;
        }
      }
    }
    
    return true;
  }
};


class Solution {
  vector<bool> visited;
  vector<vector<int>> adj;
  decltype(std::chrono::high_resolution_clock::now()) s;
  decltype(std::chrono::high_resolution_clock::now()) e;      
  
  bool dfs(int node, vector<bool>& path) {    
    s = chrono::high_resolution_clock::now();
    path[node] = visited[node] = true;
    e = chrono::high_resolution_clock::now();
    cout << "Insert: " << duration_cast<nanoseconds>(e - s).count() << endl;


    for (auto &neighbor : adj[node]) {
      s = chrono::high_resolution_clock::now();
      if (path[neighbor]) {
        return true;
      }
      e = chrono::high_resolution_clock::now();
      cout << "Find: " << duration_cast<nanoseconds>(e - s).count() << endl;      

      if (visited[neighbor]) {
        continue;
      }

      auto s = std::chrono::high_resolution_clock::now();
      vector<bool> path_branch = path;
      auto e = std::chrono::high_resolution_clock::now();
      cout << "Copy: " << duration_cast<nanoseconds>(e - s).count() << endl;

      if (dfs(neighbor, path_branch)) {
        return true;
      }
    }

    return false;
  }
public:
  bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
    // basically we need to make sure there are no dependency cycles between
    // classes. we can do dfs cycle detection or we can try to
    // do a topological sort

    visited = vector<bool>(numCourses);
    adj = vector<vector<int>>(numCourses, vector<int>());

    for (auto &p : prerequisites) {
      adj[p[0]].push_back(p[1]);
    }
    
    for (int i = 0; i < numCourses; i++) {
      if (!visited[i]) {
        auto path = vector<bool>(numCourses);
        if (dfs(i, path)) {
          return false;
        }
      }
    }
    
    return true;
  }
};

int main() {
	auto pre = vector<vector<int>>{{1,0},{1,0}};
	Solution().canFinish(2, pre);
}
