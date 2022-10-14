# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        newRoot = None
        def dfs(node):
            nonlocal newRoot
            if node.val == p.val or node.val == q.val:
                newRoot = node
                return True
            
            left, right = None, None
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            if left and right:
                newRoot = node
                return True
            if left or right:
                return True
            
        dfs(root)
        return newRoot
        