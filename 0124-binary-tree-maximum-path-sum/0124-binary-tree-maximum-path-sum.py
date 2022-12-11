# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, cur, ans):
        if not cur:
            return 0
        left = self.pathSum(cur.left, ans)
        right = self.pathSum(cur.right, ans)
        c1 = left + cur.val
        c2 = right + cur.val
        ans[0] = max(ans[0], cur.val)
        bst = max(c1, c2)
        ans[0] = max(ans[0], bst)
        ans[0] = max(left + right + cur.val, ans[0])
        return max(cur.val, max(left, right) + cur.val)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]
        self.pathSum(root, ans)
        return ans[0]
        
        