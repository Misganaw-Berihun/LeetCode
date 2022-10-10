# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(gpar, par, node):
            if not node:
                return 0
            
            left = dfs(par, node, node.left)
            right = dfs(par, node, node.right)
            temp = 0
            if gpar and gpar.val % 2 == 0:
                temp = node.val
            return left + right + temp
            
        return dfs(None, None, root)
        