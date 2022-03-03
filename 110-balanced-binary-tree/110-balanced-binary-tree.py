# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(rt):
            if not rt:
                return 0
            
            left = 1 + balanced(rt.left)
            right = 1 + balanced(rt.right)
            
            if abs(right - left) > 1:
                self.isBal = False
            
            return max(left,right)
        
        self.isBal = True
        balanced(root)
        return self.isBal
        