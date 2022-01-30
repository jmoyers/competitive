#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Node {
 public:
  int val;
  vector<Node*> neighbors;

  Node() {
    val = 0;
    neighbors = vector<Node*>();
  }

  Node(int _val) {
    val = _val;
    neighbors = vector<Node*>();
  }

  Node(int _val, vector<Node*> _neighbors) {
    val = _val;
    neighbors = _neighbors;
  }
};

class Solution {
  unordered_map<Node *, Node *> copies;
public:
  Node* cloneGraph(Node* node) {
    if (node == nullptr) return nullptr;
    if (copies.find(node) == copies.end()) {
      copies[node] = new Node(node->val);
      for (auto *n : node->neighbors) {
        copies[node]->neighbors.emplace_back(cloneGraph(n));
      }
    } 
    
    return copies[node];
  }
};


int main() {
  vector<Node *> neighbors;
  neighbors.emplace_back(new Node(1));
  neighbors.emplace_back(new Node(2));
  neighbors.emplace_back(new Node(3));
  neighbors.emplace_back(new Node(5));
  Node root(4, neighbors);
  auto clone = Solution().cloneGraph(&root);

  cout << clone->val << endl;
  for (auto *n : clone->neighbors) {
    cout << n->val << endl;
  }

  return 0;
}
