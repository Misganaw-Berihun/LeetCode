# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        h1 = head
        fast = head
        slow = head
        twin_sum = 0
        
        #find the middle of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
  
        cur = slow.next
        prev = slow
        
        #reverse the right half of the linked list
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        slow.next = None
         
        #sum each twin and find the max
        while prev :
            twin_sum = max(twin_sum, prev.val + h1.val)
            h1 = h1.next
            prev = prev.next
            
        return twin_sum
            
            
            
            
        
            
        