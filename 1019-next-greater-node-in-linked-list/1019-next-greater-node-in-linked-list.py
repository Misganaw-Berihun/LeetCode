# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        ans = []
        i = 0
        
        cur = head
        
        while cur:
            ans.append(0)
            cur = cur.next
            
        while head:
            value = head.val
            while stack and stack[-1][0] < value:
                popped = stack.pop()
                ans[popped[1]] = value
                
            stack.append((head.val,i))
            i += 1
            head = head.next
            
        return ans
            
            
            
            
        
        
        
        