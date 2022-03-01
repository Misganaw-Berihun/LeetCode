# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = []
        ans = []
        visited = set()
        stack.append(root)
        
        while stack:
            top = stack[-1]
            
            if top.left and top.left not in visited:
                stack.append(top.left)
            elif top.right and top.right not in visited:
                stack.append(top.right)
            else:
                visited.add(top)
                ans.append(top.val)
                stack.pop()
                
        return ans
            
        