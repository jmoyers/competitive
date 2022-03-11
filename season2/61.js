/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} h
 * @param {number} k
 * @return {ListNode}
 */
const rotateRight = (h, k) => {
  if (!h || !h.next || !k) return h;

  let map = [];

  let curr = h;

  while (curr) {
    map.push(curr);
    curr = curr.next;
  }

  const end = map.length - (k % map.length) - 1;

  //console.log(end, k, map.length);

  map[map.length - 1].next = h;
  map[end].next = null;

  const head = end + 1 >= map.length ? 0 : end + 1;

  return map[head];
};
