// Reverse a singly linked list.
//
// Example:
//
// Input: 1->2->3->4->5->NULL
// Output: 5->4->3->2->1->NULL
//
// Follow up:
//
// A linked list can be reversed either iteratively or recursively. Could you
// implement both?

const { ListNode, linkedFromArray, arrayFromLinked } = require("./ll.js");

const reverseList = head => {
  if (!head) return head;

  let prev = null;
  let curr = head;
  let next = head.next;

  while (curr) {
    curr.next = prev;

    prev = curr;
    curr = next;
    next = next ? next.next : null;
  }

  return prev;
};

const rec = head => {
  if (!head) return head;

  const helper = (prev, curr, next) => {
    if (!curr) return prev;

    curr.next = prev;
    prev = curr;
    curr = next;
    next = next ? next.next : null;
    return helper(prev, curr, next);
  };

  return helper(null, head, head.next);
};

let input = linkedFromArray([1, 2, 3, 4, 5]);
let output = rec(input);
console.log(output);
console.log(arrayFromLinked(output));
