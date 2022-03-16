# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        ans = 0
        stk = []
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        while slow:
            stk.append(slow)
            slow = slow.next
            
        while stk:
            ans = max(ans,stk.pop().val + head.val)
            head = head.next
            
        return ans
            
        
        