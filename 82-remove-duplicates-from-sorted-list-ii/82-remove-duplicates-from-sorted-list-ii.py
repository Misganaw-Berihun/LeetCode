# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        cur = head.next
        temp = head
        p = None
        duplicate = set()
        
        while cur:
            if temp.val == cur.val:
                duplicate.add(temp.val)
            else:
                #if temp.val has no duplicate
                if temp.val not in duplicate:
                    if p:
                        p.next = temp
                        p = p.next
                    else:
                        p = temp
                        dummy.next = p
                   
                #if the last element is unique
                if cur.next == None:
                    if p:
                        p.next = cur
                        p = p.next
                    else:
                        p = cur
                        dummy.next = p
                        
                temp = cur    
            cur = cur.next
        
        if p:
            p.next = None
            
        return dummy.next
            
        
                    
                    
                    
                    
            
                
                
        
        
        