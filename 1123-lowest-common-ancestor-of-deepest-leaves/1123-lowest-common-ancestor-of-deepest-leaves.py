# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(rt,depth):
            if not rt:
                return (rt,depth - 1)
            
            left = dfs(rt.left,depth + 1)
            right = dfs(rt.right,depth + 1)
            
            if left[1] > right[1]:
                return left
            if right[1] > left[1]:
                return right
            else:
                return (rt,left[1])
            
        return dfs(root,0)[0]
    
        