# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lead = lag = dummy
        
        for i in range(k + 1):
            lead = lead.next
            
        while lead:
            lead = lead.next
            lag = lag.next
           
        cur = dummy
        for i in range(k - 1):
            cur = cur.next
        
        tmp = cur.next.val
        cur.next.val = lag.next.val
        lag.next.val = tmp
        
        return dummy.next
        
            
        
        
        
        