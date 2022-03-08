/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public void flatten(TreeNode root) {
        TreeNode current = root;
        Stack<TreeNode> stk = new Stack<>();
        TreeNode newHead = new TreeNode(0);
        TreeNode trav = newHead;
        TreeNode temp = null;
        
        while (!stk.empty() || current != null){
            temp = current;
            newHead.right = current;
            newHead.left = null;
            newHead = newHead.right;
            
            if (temp!= null && temp.right != null){
                stk.push(temp.right);
            }
            current = temp.left;
            
            if (!stk.empty() && current==null){
                current = stk.pop();
            } 
        }
        
        root = newHead.right;
    }
}