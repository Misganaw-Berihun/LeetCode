# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, node):
        prev = None
        cur = node
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left_node = right_node  = dummy
        
        for i in range(left - 1):
            left_node = left_node.next
            
        for j in range(right):
            right_node = right_node.next
            
        right_nxt = right_node.next
        left_nxt = left_node.next
        right_node.next = None
        left_node.next = self.reverse(left_node.next)
        left_nxt.next = right_nxt
        return dummy.next
        