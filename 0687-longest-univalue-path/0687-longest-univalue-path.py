# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def lup(cur, parent):
            nonlocal ans
            if not cur:
                return 0
            
            left = lup(cur.left, cur.val)
            right = lup(cur.right, cur.val)
            ans = max(left + right, ans)
            ret = 0
            if cur.val == parent:
                ret = max(left, right) + 1
            return ret
        
        ans = 0
        lup(root, -1)
        return ans