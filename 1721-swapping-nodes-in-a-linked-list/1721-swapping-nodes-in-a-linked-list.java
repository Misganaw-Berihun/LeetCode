/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        ListNode fast = head, slow = head, k_from_st = null;
        int i = k - 1;
        
        while (fast != null && i-- > 0){
            fast = fast.next;
        }
        
        k_from_st = fast;
        fast = fast.next;
        while (fast != null){
            fast = fast.next;
            slow = slow.next;
        }        
        
        int temp = slow.val;
        slow.val = k_from_st.val;
        k_from_st.val = temp;
        
        return head;
    }
}