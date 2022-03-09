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
var deleteDuplicates = function (head) {
  if (!head || !head.next) return head;

  let dummy = new ListNode(head.val, head);
  let curr = head;
  let last = dummy;

  while (curr) {
    //console.log('curr', last, curr);
    if (curr.next && curr.val === curr.next.val) {
      let end = curr.next;
      while (end && curr.val === end.val) {
        end = end.next;
      }
      last.next = end;
      curr = end;
    } else {
      last = curr;
      curr = curr.next;
    }
  }

  return dummy.next;
};
