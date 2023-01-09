# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)
        before = before_head
        after_head = ListNode(0)
        after = after_head
        cur = head
        
        while cur:
            new_node = ListNode(cur.val)
            if cur.val < x:
                before.next = new_node
                before = before.next
            else:
                after.next = new_node
                after = after.next
        
            cur = cur.next
        
        before.next = after_head.next
        return before_head.next
  
        
        