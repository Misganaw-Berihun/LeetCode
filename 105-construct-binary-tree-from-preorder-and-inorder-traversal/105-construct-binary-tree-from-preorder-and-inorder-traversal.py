# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r or in_l > in_r:
                return None
            idx = cache[preorder[pre_l]]
            left = dfs(pre_l + 1, pre_l + (idx - in_l), in_l, idx - 1)
            right = dfs(pre_l + (idx - in_l) + 1, pre_r, idx + 1, in_r)
            return TreeNode(preorder[pre_l], left, right)
        
        cache = {}
        n = len(preorder)
        for i, val in enumerate(inorder):
            cache[val] = i
        return dfs(0, n - 1, 0, n - 1)
        