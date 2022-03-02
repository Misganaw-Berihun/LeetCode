# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(rt):
            if not rt or (not rt.left and not rt.right):
                return rt
            
            temp = rt.left
            rt.left = invert(rt.right)
            rt.right = invert(temp)
                        
            return rt
        
        return invert(root)