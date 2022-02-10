# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head.next
        p1 = head
        
        while p:
            prev = head
            cur = head
            
            if p1.val <= p.val:
                p1 = p
                p = p.next
                continue
                
            p1.next = p.next
            while cur!= p1.next and cur.val <= p.val:
                prev = cur
                cur = cur.next
            
            if cur == head:
                p.next = head
                head = p
            else:
                p.next = cur
                prev.next = p
        
            p1 = p
            p = p.next
                        
        return head
            
        