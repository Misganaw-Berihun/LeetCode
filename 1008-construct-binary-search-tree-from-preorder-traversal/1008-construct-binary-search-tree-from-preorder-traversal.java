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
    public TreeNode bstFromPreorder(int[] preorder)
    {
        Stack<TreeNode> stk = new Stack<>();
        TreeNode cur = null;
        TreeNode root = new TreeNode(preorder[0]);
        
        stk.push(root);
        for (int i = 1; i < preorder.length; i++)
        {
            cur = new TreeNode(preorder[i]);
        
            if (!stk.empty() && stk.peek().val > cur.val)
            {
                    stk.peek().left = cur;
                    stk.push(cur);
            }
            else  if (!stk.empty() && stk.peek().val < cur.val)
            {
                TreeNode top = null;
                while(!stk.empty() && stk.peek().val < cur.val )
                {                
                    top = stk.pop();
                }
                top.right = cur;
                stk.push(cur);
            }
        }
        return root;        
    }
}