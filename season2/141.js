/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
const hasCycle = (head) => {
  if (!head || !head.next) return false;
  let slow = head,
    fast = head.next.next;

  while (fast) {
    if (slow === fast) return true;

    slow = slow.next;
    fast = fast.next;
    if (!fast) return false;
    fast = fast.next;
  }

  return false;
};
