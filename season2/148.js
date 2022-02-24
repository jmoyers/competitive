/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
const sortList = (head) => {
  if (!head) return head;

  const map = {};

  let curr = new ListNode(undefined, head);

  while ((curr = curr.next)) {
    if (map[curr.val]) {
      map[curr.val].push(curr);
    } else {
      map[curr.val] = [curr];
    }
  }

  let last = null;

  const keys = Object.keys(map)
    .sort((a, b) => a - b)
    .reverse();

  for (const k of keys) {
    for (const n of map[k]) {
      n.next = last;
      last = n;
    }
  }

  const firstKey = keys[keys.length - 1];
  const firstNode = map[firstKey][map[firstKey].length - 1];

  letcurr = firstNode;

  return firstNode;
};
