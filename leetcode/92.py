class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}->{self.next.__str__()}"


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 1 2 3 4 5, m = 1, n = 5
        # 1 = start
        # 2 = end (the new end of the reversed sequence)

        # loop pointers
        # prev, curr, next
        # first reversal should happen when
        # curr = 3, so we should have iterated 3 times when m = 2
        # reverse the links to and from curr, increment

        # after we've reversed the sequence
        # 1. point start to curr
        # 2. point end to next

        start = None
        end = head

        prev = None
        curr = head
        next = curr.next

        count = 1

        while curr and count < m:
            count += 1

            start = end
            end = start.next

            prev = curr
            curr = curr.next
            next = curr.next

        while curr and count <= n:
            next = curr.next

            # reverse
            curr.next = prev

            # move 1 forward
            prev = curr
            curr = next

            count += 1

        if start:
            start.next = prev
        end.next = curr

        if m != 1:
            return head
        else:
            return prev


def test_lc1():
    inp = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    Solution().reverseBetween(inp, 2, 4)

