# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        decimal = 0
        
        while cur:
            decimal = decimal * 2 + cur.val
            cur = cur.next
        
        return decimal
        
        