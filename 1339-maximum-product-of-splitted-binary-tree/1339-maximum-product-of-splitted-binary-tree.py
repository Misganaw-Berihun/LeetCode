# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSum(self, root):
        if not root:
            return 0
        left = self.findSum(root.left)
        right = self.findSum(root.right)
        return left + right + root.val
    
    def maxP(self, cur, mx, s):
        if not cur:
            return 0
        
        left = self.maxP(cur.left, mx, s)
        right = self.maxP(cur.right, mx, s)
        
        summ = left + right + cur.val
        mx[0] = max(summ *(s - summ), mx[0])
        return summ
    
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        summ = self.findSum(root)
        ans = [0]
        MOD = 1_000_000_007
        self.maxP(root, ans, summ)
        return ans[0] % MOD