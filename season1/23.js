// Merge k sorted linked lists and return it as one sorted list. Analyze and
// describe its complexity.
//
// Example:
//
// Input:
// [
//   1->4->5,
//   1->3->4,
//   2->6
// ]
// Output: 1->1->2->3->4->4->5->6

// create a priority queue, add the first elements from each list
// because its sorted already, you only need to hold k elements to comare
// one element from each list to find the next smallest in the whole
// dataset. the size of the PQ is O(k).
// insertion into a pq is O(log k), extraction is the same
// for each item added you are inserting it once and extracting it once
// therefore totally we should be seeing O(n * log k) running time worst case
const arrToList = arr => {
  let dummy = new ListNode(-1);

  let curr = dummy;

  while (arr.length) {
    curr.next = new ListNode(arr.shift());
    curr = curr.next;
  }

  return dummy.next;
};

const listToArr = list => {
  const result = [];

  let curr = list;

  while (curr) {
    result.push(curr.val);
    curr = curr.next;
  }

  return result;
};

const swap = (store, a, b) => {
  let tmp = store[a];
  store[a] = store[b];
  store[b] = tmp;
};

class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

class PQ {
  constructor() {
    this.store = [];
  }
  add(val, node) {
    this.store.push({ val, node });

    // bubble up until its in the correct position
    let index = this.store.length - 1;
    let parent = Math.floor((index - 1) / 2);

    while (parent >= 0 && this.store[parent].val > this.store[index].val) {
      swap(this.store, parent, index);
      index = parent;
      parent = Math.floor((index - 1) / 2);
    }
  }
  extract() {
    // swap root with last element, sink the new root down to where
    // it belongs in the tree

    if (this.store.length === 0) return null;
    if (this.store.length === 1) return this.store.pop();

    swap(this.store, 0, this.store.length - 1);

    const result = this.store.pop();

    // sink the new root down to its appropriate level
    let index = 0;
    let children = index * 2 + 1;

    while (children < this.store.length) {
      let swapto = -1;

      if (
        this.store[children + 1] &&
        this.store[children + 1].val < this.store[children].val &&
        this.store[children + 1].val < this.store[index].val
      ) {
        swapto = children + 1;
      } else if (this.store[children].val < this.store[index].val) {
        swapto = children;
      }

      if (swapto === -1) break;

      swap(this.store, index, swapto);

      index = swapto;
      children = swapto * 2 + 1;
    }

    return result;
  }
}

const mergeKLists = lists => {
  if (lists.length === 0) return null;
  if (lists.length === 1) return lists[0];

  let pq = new PQ();

  for (let l of lists) {
    if (l) pq.add(l.val, l);
  }

  let dummy = new ListNode(-1);
  let curr = dummy;

  while (pq.store.length) {
    let item = pq.extract();

    curr.next = item.node;

    if (item.node.next) {
      pq.add(item.node.next.val, item.node.next);
    }

    curr = curr.next;
  }

  return dummy.next;
};
let input = [
  arrToList([-8, -7, -7, -5, 1, 1, 3, 4]),
  arrToList([-2]),
  arrToList([-10, -10, -7, 0, 1, 3]),
  arrToList([2])
];
console.log(listToArr(mergeKLists(input)));

// [
//   1->4->5,
//   1->3->4,
//   2->6
// ]
// Output: 1->1->2->3->4->4->5->6
