// You are given two non-empty linked lists representing two non-negative
// integers. The digits are stored in reverse order and each of their nodes
// contain a single digit. Add the two numbers and return it as a linked list.
//
// You may assume the two numbers do not contain any leading zero, except the
// number 0 itself.
//
// Example:
//
// Input:
// (2 -> 4 -> 3) + (5 -> 6 -> 4)
//
// Output:
// 7 -> 0 -> 8
//
// Explanation:
// 342 + 465 = 807.
//

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

const numFromList = head => {
  let n = 0;
  let place = 1;

  while (head) {
    n += head.val * place;
    place = place * 10;
    head = head.next;
  }

  return n;
};

const listFromNum = n => {
  let remaining = n;

  const sumList = new ListNode();

  let place = 1;

  let nextVal = ((n % (place * 10)) - (n % place)) / place;
  let node = new ListNode(nextVal);

  const head = node;

  remaining = remaining - nextVal * place;

  while (remaining > 0) {
    place = place * 10;
    nextVal = ((n % (place * 10)) - (n % place)) / place;
    node.next = new ListNode(nextVal);
    node = node.next;
    remaining = remaining - nextVal * place;
  }

  return head;
};

const linkedFromArray = arr => {
  let curr = new ListNode(arr.pop());
  let head = curr;

  while (arr.length) {
    curr.next = new ListNode(arr.pop());
    curr = curr.next;
  }

  return head;
};

const arrayFromLinked = head => {
  let result = [];

  while (head) {
    result.push(head.val);
    head = head.next;
  }

  return result;
};

const addTwoNumbers = (l1, l2) => {
  let head = null;
  let curr = null;
  let carry = 0;

  while (l1 || l2 || carry) {
    let next = new ListNode();

    let n1 = l1 ? l1.val : 0;
    let n2 = l2 ? l2.val : 0;
    let sum = n1 + n2 + carry;
    carry = 0;

    if (sum > 9) {
      carry = 1;
      sum = sum - 10;
    }

    next.val = sum;

    if (!head) {
      curr = next;
      head = next;
    } else {
      curr.next = next;
      curr = curr.next;
    }

    if (l1) l1 = l1.next;
    if (l2) l2 = l2.next;
  }

  return head;
};

let l1 = linkedFromArray([9]);
let l2 = linkedFromArray([9]);
//let l1 = linkedFromArray([2, 4, 3]);
//let l2 = linkedFromArray([5, 6, 4]);
let head = addTwoNumbers(l1, l2);

console.log(arrayFromLinked(head));
