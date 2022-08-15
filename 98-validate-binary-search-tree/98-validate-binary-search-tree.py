# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(rt):
            nonlocal status
            if not rt:
                return (float('-inf'), float('inf'))
            
            left = rec(rt.left)
            right = rec(rt.right)
            
            if left[0] >= rt.val or rt.val >= right[1]:
                status = False
                
            return (max(left[0], right[0], rt.val), min(left[1], right[1], rt.val))
        
        status = True
        rec(root)
        return status
        