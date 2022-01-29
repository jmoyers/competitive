#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
  unordered_set<int> cycle;
  unordered_set<int> visited;
  unordered_map<int, vector<int>> adj;
  vector<int> topo;
  
  // we return false if there is a cycle and therefore not possible
  // to have a valid topo sort
  bool dfs(int &node) {
    visited.insert(node);
    cycle.insert(node);

    for (auto &neighbor : adj[node]) {
      if (cycle.find(neighbor) != cycle.end()) {
        return false;
      }

      if (visited.find(neighbor) != visited.end()) {
        continue;
      }

      if (!dfs(neighbor)) {
        return false;
      }

    }

    cycle.erase(node);
    topo.push_back(node);

    return true;
  }
 public:
  vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
    // create adjacency list, required for both cycle detection and topo
    for (auto &p : prerequisites) {
      adj[p[0]].push_back(p[1]);
    }

    // the only way we couldn't finish the course is if there is a cycle
    // in the courses prerequisites, so we have to do some cycle detection

    // cycle detection

    // within one dfs branch, you should never encounter the root of that
    // branch again in the dfs.

    // store a visited set that gets passed down per branch
    // check your visited set all the way to the leaf nodes
    // if you ever encounter a duplicate item, you have a cycle
    // and its not possible to complete

    // assuming no cycles - we now need a valid course ordering
    // the way we do that is thru a topological graph sort.
    
    // topological sort

    // dfs
    // need a visited set

    // once you fully explore a node, you can add it to a stack
    // such that leaf nodes get pushed on to the stack first

    // explore all nodes (some can be unconnected, make sure they are
    // not already in the visited set

    for (auto i = 0; i < numCourses; i++) {
      if (visited.find(i) == visited.end()) {
        if (!dfs(i)) {
          return vector<int>{};
        }
      }
    }


    return topo;
  }
};

void test_1() {
  vector<vector<int>> prereqs{{1,0}};
  auto topo = Solution().findOrder(2, prereqs);

  for (auto &c : topo) 
    cout << c << endl;
}

void test_2() {
  // 4, [[1,0],[2,0],[3,1],[3,2]]
  vector<vector<int>> prereqs{{1,0}, {2,0}, {3,1}, {3,2}};
  auto topo = Solution().findOrder(4, prereqs);

  for (auto &c : topo) 
    cout << c << endl;
}

void test_cycle() {
  // 4, [[1,0],[2,0],[3,1],[3,2]]
  vector<vector<int>> prereqs{{1,0}, {0,1}};
  auto topo = Solution().findOrder(2, prereqs);

  for (auto &c : topo) 
    cout << c << endl;
}

int main() {
  test_1();
  test_2();
  test_cycle();
}
