# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def traverse(par,grand):
            if not par:
                return
            
            if grand and grand.val % 2==0:
                left = par.left.val if par.left else 0
                right = par.right.val if par.right else 0
                
                self.ans += left + right
                
            traverse(par.left,par)
            traverse(par.right,par)
            
        self.ans = 0
        traverse(root,None)
        return self.ans
            
            
        