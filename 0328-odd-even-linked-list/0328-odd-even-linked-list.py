# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before_odd = ListNode(0)
        before_even = ListNode(0)
        odd = before_odd
        even = before_even
        cur = head
        flag = True
        
        while cur:
            new_node = ListNode(cur.val)
            if flag:
                odd.next = new_node
                odd = odd.next
            else:
                even.next = new_node
                even = even.next
            
            flag = not flag
            cur = cur.next
        
        odd.next = before_even.next
        return before_odd.next