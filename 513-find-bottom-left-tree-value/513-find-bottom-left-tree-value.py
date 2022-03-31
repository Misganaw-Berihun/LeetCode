# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(rt, level):
            if not rt:
                return (rt, level - 1)
            left = dfs(rt.left, level + 1)
            right  = dfs(rt.right , level + 1)
            
            if  left[1] >= right[1]:
                if left[1] == level and left[0] == None:
                    return (rt, level)
                return left
            else:
                if right[1] == level and right[0] == None:
                    return (rt, level)
                return right
        return dfs(root,0)[0].val
        
            
        