# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = curr = ListNode()
        
        while l1 or l2:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            carry = total // 10
            if carry:
                total = total % 10
            
            curr.next = ListNode(total)
            curr = curr.next
        
        if carry:
            curr.next = ListNode(carry)
            curr = curr.next
        
        return head.next
            
            
            
            
                
        
