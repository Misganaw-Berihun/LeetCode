# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy
        
        for i in range(left - 1):
            pre = pre.next
            
        tail = pre.next
        for i in range(right - left):
            temp = pre.next
            pre.next = tail.next
            tail.next = tail.next.next
            pre.next.next = temp
            
        return dummy.next
        