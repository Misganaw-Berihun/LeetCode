# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, cur):
        if not cur or not cur.next:
            return cur
        
        node = self.reverse(cur.next)
        cur.next.next = cur
        cur.next = None
        return node
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head)