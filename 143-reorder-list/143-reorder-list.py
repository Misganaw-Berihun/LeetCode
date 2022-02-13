# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        cur = head
        stack = []
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        trav = slow
        while trav:
            stack.append(trav)
            trav = trav.next
            
        while cur != slow and stack:
            temp = cur.next
            top = stack.pop()
            cur.next = top
            top.next = temp
            cur = temp
            
        cur.next = None
        return head
            
        
        
            
            
        
        