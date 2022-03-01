# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        top = root
        visited = set()
        ans = []
        
        while root:
            stack.append(root)
            visited.add(root)
            root = root.left
            
        while stack:
            top = stack[-1]
            stack.pop()
            
            if top.left and top.left not in visited:
                stack.append(top)
                visited.add(top.left)
                stack.append(top.left)
            elif top.right:
                ans.append(top.val)
                visited.add(top)
                stack.append(top.right)
            else:
                ans.append(top.val)
        return ans
                
                
                
                
                
            
            
        