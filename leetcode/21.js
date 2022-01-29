function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

const mergeTwoLists = function(l1, l2) {
  let dummy = new ListNode(-1);
  let curr = dummy;

  while (l1 || l2) {
    if (!l1) {
      curr.next = l2;
      l2 = null;
      break;
    }

    if (!l2) {
      curr.next = l1;
      l1 = null;
      break;
    }

    if (l1.val < l2.val) {
      let wasNext = l1.next;
      l1.next = null;
      curr.next = l1;
      l1 = wasNext;
    } else {
      let wasNext = l2.next;
      l2.next = null;
      curr.next = l2;
      l2 = wasNext;
    }

    curr = curr.next;
  }

  return dummy.next;
};
