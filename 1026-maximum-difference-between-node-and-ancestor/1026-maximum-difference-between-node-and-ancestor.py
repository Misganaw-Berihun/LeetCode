# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDiff(self, cur, ans):
        if not cur:
            return (-inf, inf)
        left = self.maxDiff(cur.left, ans)
        right = self.maxDiff(cur.right, ans)
        if left != (-inf, inf):
            d1 = abs(cur.val - left[0])
            d2 = abs(cur.val - left[1])
            ans[0] = max(d1, d2, ans[0])
        if right != (-inf, inf):
            d1 = abs(cur.val - right[0])
            d2 = abs(cur.val - right[1])
            ans[0] = max(d1, d2, ans[0])
        mx = max(left[0], right[0], cur.val)
        mn = min(left[1], right[1], cur.val)
        return (mx, mn)
    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = [-inf]
        self.maxDiff(root, ans)
        return ans[0]