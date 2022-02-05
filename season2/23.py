# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge a pair of lists at a time a la merge sort
        if not lists:
            return None
        
        queue = deque(lists)
        
        while len(queue) > 1:
            l1 = queue.popleft()
            l2 = queue.popleft()
            queue.append(self.mergeListPair(l1, l2))
        
        return queue[0]
        
    def mergeListPair(self, list1, list2):
        dummy = ListNode(-math.inf)
        head = dummy
        
        while list1 or list2: 
            if list1:
                if not list2 or list1.val <= list2.val:
                    tmp = list1.next
                    list1.next = None
                    head.next = list1
                    list1 = tmp
                    print(head)
                    head = head.next
            
            if list2:
                if not list1 or list2.val <= list1.val:
                    tmp = list2.next
                    list2.next = None
                    head.next = list2
                    list2 = tmp
                    head = head.next
         
        return dummy.next
