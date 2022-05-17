# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stk = []
        stk.append((root, 1))
        res = float('inf')
        
        while stk:
            node, level = stk.pop()
            
            if node and not node.left and not node.right:
                res = min(res, level)
            if node:
                if node.left:
                    stk.append((node.left, level + 1))
                if node.right:
                    stk.append((node.right, level + 1))
                    
        return res
            
            
        