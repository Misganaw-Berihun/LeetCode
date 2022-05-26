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
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null){
            return new ArrayList<Integer>();
        }
        ArrayDeque<TreeNode> queue = new ArrayDeque();
        List<Integer> ans = new ArrayList<>();
        queue.addLast(root);
        
        while (!queue.isEmpty()){
            int n = queue.size();
            TreeNode cur = null;
            
            for (int i = 0; i < n; ++i){
                cur = queue.pollFirst();
                if (cur.left != null){
                    queue.addLast(cur.left);
                }
                if (cur.right != null){
                    queue.addLast(cur.right);
                }
            }
            ans.add(cur.val);
        }
        return ans;
    }
}