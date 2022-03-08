# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def tilt(rt):
            if not rt.left and not rt.right:
                return rt.val
            
            left = tilt(rt.left) if rt.left else 0
            right = tilt(rt.right) if rt.right else 0
            
            t = abs(right - left)
            self.total += t
            
            return rt.val + left + right
        
        if not root or (not root.left and not root.right):
            return 0
        
        self.total = 0
        tilt(root)
        return self.total
        
        

        
        