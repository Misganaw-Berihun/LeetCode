# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        if not head or head.next == None:
            return head
        else:
            p = self.reverse(head.next)
            head.next.next = head
            head.next = None
            
            return p
            
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        h1 = head
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        h2 = self.reverse(slow)
        
        while h2:
            if h1.val != h2.val:
                return False
            h2 = h2.next
            h1 = h1.next
            
        return True
        
        
        
        
        