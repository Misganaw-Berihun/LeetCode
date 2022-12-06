# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_part = ListNode(0)
        dummy = ListNode(0)
        dummy.next = even_part
        new_head = ListNode(0)
        odd_part = ListNode(0)
        new_head.next = odd_part
        cur = head
        cnt = 0
        
        while cur:
            nxt = cur.next
            if cnt % 2 == 0:
                odd_part.next = cur
                odd_part = odd_part.next
            else:
                even_part.next = cur
                even_part = even_part.next
            cur.next = None
            cur = nxt
            cnt += 1
        
        odd_part.next = dummy.next.next
        return new_head.next.next
        