# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = head
        
        while cur:
            temp = cur
            while cur and cur.val == temp.val:
                cur = cur.next
            
            temp.next = cur
        
        return dummy.next
        