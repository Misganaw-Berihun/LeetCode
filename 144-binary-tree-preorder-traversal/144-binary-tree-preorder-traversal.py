# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = []
        ans = []
        visited = set()
        stack.append(root)
        visited.add(root)
        ans.append(root.val)
        
        while stack:
            top = stack[-1]
            
            if top.left and top.left not in visited:
                ans.append(top.left.val)
                visited.add(top.left)
                stack.append(top.left)
            elif top.right and top.right not in visited:
                ans.append(top.right.val)
                visited.add(top.right)
                stack.append(top.right)
            else:
                stack.pop()
                
        return ans
            