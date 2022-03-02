# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0
        self.totalSum = 0
        
        def helper(rt,isLeft):
            if rt is None:
                return 
            
            if not rt.left and not rt.right  and isLeft:
                self.totalSum += rt.val
            
            helper(rt.left,True)
            helper(rt.right,False)
            
        helper(root,True)
        return self.totalSum
            
                
                
        