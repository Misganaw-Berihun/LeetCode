# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def findSum(gp, p, c):
            nonlocal summ
            if not c:
                return
            
            if gp % 2 == 0:
                summ += c.val
                
            findSum(p, c.val, c.left)
            findSum(p, c.val, c.right)
            
        summ = 0
        findSum(1, 1, root)
        return summ