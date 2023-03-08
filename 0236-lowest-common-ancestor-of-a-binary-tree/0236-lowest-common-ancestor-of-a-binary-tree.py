# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(rt):
            nonlocal node
            if not rt:
                return 0
            
            left = lca(rt.left)
            right = lca(rt.right)
            
            summ = left + right
            if rt.val == p.val or rt.val == q.val:
                summ += 1 
            
            if summ == 2 and not node:
                node = rt
            
            return summ
        
        node = None
        lca(root)
        return node
        