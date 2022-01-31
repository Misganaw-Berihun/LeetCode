# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        
        if head == None: 
            return head 
        
        stack.append(head)
        cur = head.next
        head.next = None
        
        while cur != None:
            temp = cur.next
            cur.next = stack.pop()
            stack.append(cur)
            cur = temp
            
        return stack.pop()
            
        
            
        
        