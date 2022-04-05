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
            inord.append(rt)
            inorder(rt.right)
            
        inord = []
        inorder(root)
        p1, p2 = None, None
        
        for i in range(1,len(inord)):
            if inord[i].val < inord[i - 1].val:
                if not p1:
                    p1 = inord[i-1]
                p2 = inord[i]
                
        temp = p1.val
        p1.val = p2.val
        p2.val = temp
        
                    
                