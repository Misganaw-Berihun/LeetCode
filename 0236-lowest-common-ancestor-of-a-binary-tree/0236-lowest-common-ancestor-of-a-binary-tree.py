# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node):
            nonlocal lst
            if not node:
                return False
            
            left = lca(node.left)
            right = lca(node.right)
            cur = (node.val == p.val or node.val == q.val)
            
            if left + right + cur == 2:
                lst = node
                return True
            
            return cur or left or right
        
        lst = None
        lca(root)
        return lst
        