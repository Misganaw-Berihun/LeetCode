# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def btg(cur):
            nonlocal add
            if not cur:
                return
            
            btg(cur.right)
            cur.val += add
            add = cur.val
            btg(cur.left)
        
        add = 0
        btg(root)
        return root
        