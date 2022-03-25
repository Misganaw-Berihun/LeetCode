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
    public void insert(TreeNode root, int val){
        TreeNode prev = null, cur = root;
        boolean isLeft = true;
        
        while (cur != null){
            prev = cur;
            if (cur.val > val){
                cur = cur.left;
                isLeft = true;
            }
            else if (cur.val < val){
                cur = cur.right;
                isLeft = false;
            }
        }
        
        if (prev == null){
            root = new TreeNode(val); 
        }
        else if (isLeft){
            prev.left = new TreeNode(val);
        }
        else{
            prev.right = new TreeNode(val);
        }
    }
    
    public TreeNode bstFromPreorder(int[] preorder) {
        TreeNode root = new TreeNode(preorder[0]);
        for (int i = 1; i < preorder.length; ++i){
            insert(root, preorder[i]);
        }
        return root;
    }
}