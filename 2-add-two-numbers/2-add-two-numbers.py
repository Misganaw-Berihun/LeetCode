# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p1_val = p2_val = 0
        p2 = l2
        cur = ListNode(0,None)
        dummy = cur
        rem = 0
        
        while p1 or p2:
            res = 0
            if p1:
                p1_val = p1.val
            else:
                p1_val = 0
                
            if p2:
                p2_val = p2.val
            else:
                p2_val = 0
                
            res = p1_val + p2_val + rem
            rem = (res // 10) % 10
            
            
            cur.next = ListNode(res % 10,None)
            cur = cur.next
            
            if p1: 
                p1 = p1.next
            if p2:
                p2 = p2.next
                
        if rem:
            cur.next = ListNode(rem,None)
            
        return dummy.next
            
        