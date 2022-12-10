/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {    
public:
    int helper(TreeNode* cur, int sum, long long &ans){
        if (NULL == cur) return 0;
        int left = helper(cur->left, sum, ans);
        int right = helper(cur->right, sum, ans);
        int s = left + right + cur->val;
        long long product = 1ll * s * (sum - s);
        ans = max(ans, product);
        return s;
    }
    
    int maxProduct(TreeNode* root) {
        long long ans = 0;
        int total = helper(root, 0, ans);
        ans = 0;
        helper(root, total, ans);
        return ans % 1'000'000'007;
    }
};