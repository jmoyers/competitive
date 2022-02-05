class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        odd_head = odd = head
        even_head = even = odd.next
        
        while odd.next and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        
        return odd_head
