# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        cur = head
        i = 0
        while i < k:
            cur = cur.next
            i += 1
            
            if cur == None and i != k:
                return head
        
        temp = self.reverseKGroup(cur,k)
        
        trav = head
        prev = temp
        next = None
        
        j = 0
        while j < k:
            next = trav.next
            trav.next = prev
        
            prev = trav
            trav = next
            j += 1
        
        return prev
            
        
            
            
            
        