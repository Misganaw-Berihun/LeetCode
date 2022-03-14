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
    public TreeNode increasingBST(TreeNode root) {
        Stack<TreeNode> stk = new  Stack<>();
        TreeNode current = root;
        TreeNode dummy =new  TreeNode(0,null,null);
        TreeNode trav = dummy;
        
        while (!stk.empty() || current != null){
           
            while(current != null){
                 stk.push(current);
                current = current.left;
            }
            
            current = stk.pop();
            trav.right = current;
            current.left = null;
            trav = trav.right;
            current = current.right;
        
        }
        
        return dummy.right;
        
    }
}