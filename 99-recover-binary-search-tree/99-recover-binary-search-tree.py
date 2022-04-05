# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(rt):
            if not rt:
                return
            
            inorder(rt.left)
            if self.first == None and self.prev.val > rt.val:
                self.first = self.prev
                
            if self.first != None and self.prev.val > rt.val:
                self.second = rt
                
            self.prev = rt
                
            inorder(rt.right)
            
        self.prev = TreeNode(float('-inf'))
        self.first = None
        self.second = None
        
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
                    
                