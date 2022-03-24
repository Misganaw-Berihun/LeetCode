# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(rt,level):
            if rt == None:
                return
            
            if len(ans) == level:
                ans.append(rt.val)
            else:
                ans[level] = max(ans[level],rt.val)
                
            left = dfs(rt.left,level + 1)
            right = dfs(rt.right,level + 1)
        
        ans = []
        dfs(root,0)
        return ans
        
        
            
            
            
           
    
        
        