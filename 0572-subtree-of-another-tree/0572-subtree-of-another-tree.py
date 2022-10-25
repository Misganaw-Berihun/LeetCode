# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, node1, node2):
        if not node1 and not node2:
            return True
        
        if not node1 or not node2 or (node1.val != node2.val):
            return False
        
        left = self.check(node1.left, node2.left)
        right = self.check(node1.right, node2.right)
        return left and right
    
    def dfs(self, cur, subroot):
        if cur.val == subroot.val:
            if self.check(cur, subroot):
                return True
            
        if cur.left and self.dfs(cur.left, subroot):
            return True
        
        if cur.right and self.dfs(cur.right, subroot):
            return True
        return False
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)
        