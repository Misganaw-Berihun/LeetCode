# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tmp = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(rt):
            if rt != None:
                traverse(rt.left)
                self.tmp.append(rt.val)
                traverse(rt.right)
    
        traverse(root)
        return self.tmp[k-1]
        
                
        
                
            
        
        
        