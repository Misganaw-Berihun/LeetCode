# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        p = None
        cur = None
        
        if not list1 and not list2:
            return None
        
        if (p1 and not p2):
            return p1
            
        elif (p2 and not p1):
            return p2
        
        if  (p1.val < p2.val):
            p = p1
            cur = p1
            p1 = p1.next
        else:
            p = p2
            cur = p2
            p2 = p2.next
            
            
        while p1 or p2:
            if p1 and p2:
                if p1.val < p2.val:
                    cur.next = p1
                    p1 = p1.next
                    cur = cur.next
                else:
                    cur.next = p2
                    p2 = p2.next
                    cur = cur.next
            elif not p2:
                cur.next = p1
                break
            elif not p1:
                cur.next = p2   
                break
                
            
        return p
                    
        
                
                
            
        
        