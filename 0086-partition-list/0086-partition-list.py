# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0)
        ptr1 = None
        ptr2_head = None
        ptr2 = None
        cur = head
        
        while cur:
            new_node = ListNode(cur.val)
            if cur.val < x:
                if not ptr1:
                    ptr1 = new_node
                    dummy.next = ptr1
                else:
                    ptr1.next = new_node
                    ptr1 = ptr1.next
            else:
                if not ptr2:
                    ptr2 = new_node
                    ptr2_head = ptr2
                else:
                    ptr2.next = new_node
                    ptr2 = ptr2.next
            
            cur = cur.next
        
        if ptr1:
            ptr1.next = ptr2_head
        else:
            dummy.next = ptr2_head
        return dummy.next
  
        
        