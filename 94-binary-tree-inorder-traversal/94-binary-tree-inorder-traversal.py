# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        current = root
        
        while True:
            
            if current is not None:
                stack.append(current)
                current = current.left
            
            elif stack:
                current = stack.pop()
                ans.append(current.val)
                current = current.right
            else:
                break
                
        return ans
                
                
                
                
                
            
            
        