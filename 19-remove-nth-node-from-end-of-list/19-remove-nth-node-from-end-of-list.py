# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        
        while cur != None:
            length += 1
            cur = cur.next
            
        del_index = length - n
        cur = head
        
        for i in range (del_index - 1):
            cur = cur.next
            
        if del_index == 0:
            return head.next
        else:
            cur.next = cur.next.next
            
        return head
            
        