# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        trav = dummy
        cur = head
        
        while cur:
            
            cnt = 0
            temp = ListNode(cur.val)
            while cur and cur.val == temp.val:
                cnt += 1
                cur = cur.next
            
            if cnt == 1:
                trav.next = temp
                trav = temp
        
        return dummy.next