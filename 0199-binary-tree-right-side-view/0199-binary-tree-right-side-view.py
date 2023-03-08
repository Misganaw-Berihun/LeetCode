# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def view(rt, level, ans):
            if not rt:
                return 
            
            if level == len(ans):
                ans.append(rt.val)
            
            view(rt.right, level + 1, ans)
            view(rt.left, level + 1, ans)
        
        ans = []
        view(root, 0, ans)
        return ans
        