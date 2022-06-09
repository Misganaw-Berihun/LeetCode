# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(l, r):
            nonlocal i, n
            if l > r:
                return None
            root_val = preorder[i]
            i += 1
            root_idx = cache[root_val]
            left = dfs(l, root_idx - 1)
            right = dfs(root_idx + 1, r)
            return TreeNode(root_val, left, right)
        cache = {}
        i = 0
        n = len(preorder)
        for j, val in enumerate(inorder):
            cache[val] = j
        return dfs(0, n - 1)
        