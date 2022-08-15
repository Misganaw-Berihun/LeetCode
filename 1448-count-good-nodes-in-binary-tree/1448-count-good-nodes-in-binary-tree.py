# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def rec(rt, maxFromRt):
            if not rt:
                return 0
            
            if rt.val >= maxFromRt:
                return rec(rt.left, rt.val) + rec(rt.right, rt.val) + 1
            else:
                return rec(rt.left, maxFromRt) + rec(rt.right, maxFromRt)
        
        return rec(root, float('-inf'))                