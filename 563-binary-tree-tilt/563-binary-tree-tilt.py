# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def tilt(rt):
            if not rt:
                return 0
            
            left = tilt(rt.left) if rt.left else 0
            right = tilt(rt.right) if rt.right else 0
            
            self.total  += abs(right - left)
            
            return rt.val + left + right
        
        self.total = 0
        tilt(root)
        return self.total
        
        

        
        