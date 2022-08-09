# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxD(rt):
            if not rt:
                return 0
            
            left, right = 0, 0
            if rt.left:
                left = maxD(rt.left)
            if rt.right:
                right = maxD(rt.right)
            self.diameter = max(left + right, self.diameter)
            return max(left, right) + 1
        self.diameter = 0
        maxD(root)
        return self.diameter