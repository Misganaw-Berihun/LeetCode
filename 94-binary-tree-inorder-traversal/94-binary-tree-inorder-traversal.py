# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(rt,ans):
            if rt != None:
                traverse(rt.left,ans)
                ans.append(rt.val)
                traverse(rt.right,ans)
                
            return ans
        
        ans = []
        return traverse(root,ans)
                
        