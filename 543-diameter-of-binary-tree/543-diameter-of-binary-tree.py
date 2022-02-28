# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def rec(cur):
            if cur == None:
                return 0
            else:
                left = rec(cur.left)
                right = rec(cur.right)
                self.ans = max(self.ans,right + left)
                return max(left,right) + 1
        
        self.ans = 0
        rec(root)
        return self.ans
        