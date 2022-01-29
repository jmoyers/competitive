#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    int carry = 0;
    ListNode dummy;

    ListNode *result = &dummy;

    while (l1 || l2) {
      int val = 0;

      if (l1 && l2) {
        val = l1->val + l2->val + carry;

        l2 = l2->next;
        l1 = l1->next;
      } else if (l1) {
        val = l1->val + carry;
        l1 = l1->next;
      } else if (l2) {
        val = l2->val + carry;
        l2 = l2->next;
      }

      if (val > 9) {
        carry = 1;
        val = val - 10;
      } else {
        carry = 0;
      }

      result->next = new ListNode(val);
      result = result->next;
    }

    if (carry == 1) {
      result->next = new ListNode(1);
    }

    return dummy.next;
  }
};

void test() {
  ListNode *a = new ListNode(2, new ListNode(4, new ListNode(3)));
  ListNode *b = new ListNode(5, new ListNode(6, new ListNode(4)));
  ListNode *result = Solution().addTwoNumbers(a, b);

  while (result) {
    cout << result->val << "->";
    result = result->next;
  }

  cout << "None" << endl;
}

void test2() {
  ListNode *a = new ListNode(5);
  ListNode *b = new ListNode(5);
  ListNode *result = Solution().addTwoNumbers(a, b);

  while (result) {
    cout << result->val << "->";
    result = result->next;
  }

  cout << "None" << endl;
}

void test3() {
  ListNode *a = new ListNode(9, new ListNode(8));
  ListNode *b = new ListNode(1);
  ListNode *result = Solution().addTwoNumbers(a, b);

  while (result) {
    cout << result->val << "->";
    result = result->next;
  }

  cout << "None" << endl;
}

int main() {
  test3();
  return 0;
}
