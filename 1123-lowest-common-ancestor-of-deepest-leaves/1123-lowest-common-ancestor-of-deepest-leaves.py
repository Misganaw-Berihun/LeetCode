# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(cur):
            if not cur:
                return [None, 0]

            left = dfs(cur.left)
            right = dfs(cur.right)

            if left[1] == right[1]:
                return [cur, left[1] + 1]
            elif left[1] > right[1]:
                return [left[0], left[1] + 1]
            else:
                return [right[0], right[1] + 1]
            
        return dfs(root)[0]