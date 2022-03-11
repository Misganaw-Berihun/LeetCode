# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk1 = []
        stk2 = []
        next = None
        node = None
        
        cur = l1
        carry = 0
        
        while cur != None:
            stk1.append(cur)
            cur = cur.next
            
        cur = l2
        while cur != None:
            stk2.append(cur)
            cur = cur.next
            
        while stk1 and stk2:
            val = stk1.pop().val + stk2.pop().val + carry
            carry = val // 10
            digit = val % 10
            
            node = ListNode(digit,next)
            next = node
            
        while stk1 or stk2:
            val = 0
            if stk1:
                val = stk1.pop().val + carry
            if stk2:
                val = stk2.pop().val + carry
                
            carry = val // 10
            digit = val % 10
            
            node = ListNode(digit,next)
            next = node            
            
        if  carry > 0:
            node = ListNode(carry,next)
            next = node 
            
        return node
            
        
        
            
        