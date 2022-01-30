class ListNode {
  constructor(val, next, random) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
    this.random = random === undefined ? null : random;
  }
}

const linkedFromArray = arr => {
  let curr = new ListNode(arr.shift());
  let head = curr;

  while (arr.length) {
    curr.next = new ListNode(arr.shift());
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

module.exports = {
  ListNode,
  linkedFromArray,
  arrayFromLinked
};
