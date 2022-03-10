/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  let carry = 0,
    sum = 0,
    dummy = new ListNode();
  let curr = dummy;
  while (l1 || l2) {
    //console.log(carry, l1.val, l2 && l2.val);
    sum = 0;
    sum += carry;
    sum += l1 ? l1.val : 0;
    sum += l2 ? l2.val : 0;

    carry = 0;

    if (sum >= 10) {
      //console.log('sum', sum);
      carry = Math.floor(sum / 10);
      sum = sum % 10;
      //console.log(carry, sum);
    }

    curr.next = new ListNode(sum);
    curr = curr.next;

    if (l1) l1 = l1.next;
    if (l2) l2 = l2.next;
  }

  if (carry) curr.next = new ListNode(carry);

  return dummy.next;
};
