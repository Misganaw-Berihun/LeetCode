# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeSort(left,right):
            if right == left:
                return lists[left]
            else:
                mid = left + (right - left) // 2
                return merge(mergeSort(left,mid),mergeSort(mid+1,right))
                  
        def merge(left_list,right_list):
            dummy = ListNode(0)
            ret = dummy
            
            while left_list and right_list:
                if left_list.val < right_list.val:
                    ret.next = left_list
                    left_list = left_list.next
                else:
                    ret.next = right_list
                    right_list = right_list.next
                
                ret = ret.next
            
            ret.next = left_list if left_list else right_list
            return dummy.next
        
        if not lists:
            return None
        
        return mergeSort(0,len(lists) - 1)                   