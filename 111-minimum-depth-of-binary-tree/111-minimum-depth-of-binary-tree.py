# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        left = 1 + self.minDepth(root.left)
        right = 1 + self.minDepth(root.right)
        
        if left != 1 and right!= 1:
            return min(left,right)
        elif left != 1:
            return left
        else:
            return right
            
        