# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def addPath(rt,sofar):
            if not rt:
                return 0
            
            sofar += str(rt.val)
            if rt.right == None and rt.left == None:
                return int(sofar)
            return addPath(rt.left,sofar) + addPath(rt.right,sofar)
        
        return addPath(root,"")
        
            
            