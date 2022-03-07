const mergeTwoLists = (list1, list2) => {
  let c1 = list1,
    c2 = list2;
  let ans = new ListNode();
  const head = ans;

  while (c1 || c2) {
    if (c1 && c2) {
      if (c1.val >= c2.val) {
        ans.next = c2;
        c2 = c2.next;
      } else {
        ans.next = c1;
        c1 = c1.next;
      }
    } else if (c1) {
      ans.next = c1;
      c1 = c1.next;
    } else if (c2) {
      ans.next = c2;
      c2 = c2.next;
    }

    ans = ans.next;
  }

  return head.next;
};
