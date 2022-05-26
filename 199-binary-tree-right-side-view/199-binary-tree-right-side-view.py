# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(rt, level):
            nonlocal result
            if not rt:
                return
            
            if len(result) == level:
                result.append(rt.val)
            
            dfs(rt.right, level + 1)
            dfs(rt.left, level + 1)
        
        result = []
        dfs(root, 0)
        return result
        