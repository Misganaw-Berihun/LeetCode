# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #insert values in sorted order
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(head1,head2):
            dummy = cur = ListNode(0)
            
            while head1 and head2:
                if head1.val > head2.val:
                    cur.next = head2
                    head2 = head2.next
                else:
                    cur.next = head1
                    head1 = head1.next
                cur = cur.next
                
            cur.next = head1 if head1 else head2
            return dummy.next
                
        def mergeSort(h):
            if h == None or h.next == None:
                return h
            
            fast = h
            slow = h
            temp = h
            
            while fast and fast.next:
                fast = fast.next.next
                temp = slow
                slow = slow.next
            
            temp.next = None
            h1 = mergeSort(h)
            h2 = mergeSort(slow)
            return merge(h1,h2)
    
        return mergeSort(head)
                
            
                
            
            
            
            
        
       
            
            
            
                
        
        
        
        