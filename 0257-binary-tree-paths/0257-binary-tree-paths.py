# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def paths(rt, path):
            if not rt:
                return
            
            if not rt.left and not rt.right:
                ans.append(path + str(rt.val))
                return
            
            if rt.left:
                paths(rt.left, path + str(rt.val) + "->")
            
            if rt.right:
                paths(rt.right, path + str(rt.val) + "->")
        
        ans = []
        paths(root, "")
        return ans