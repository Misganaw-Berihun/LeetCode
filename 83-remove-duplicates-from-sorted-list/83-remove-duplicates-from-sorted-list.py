# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        p1 = head.next
        p2 = head
        
        while p1:
            if p1.val != p2.val:
                p2.next = p1
                p2 = p2.next
            p1 = p1.next
                
        if p2.next:
            p2.next = None
        
        return head