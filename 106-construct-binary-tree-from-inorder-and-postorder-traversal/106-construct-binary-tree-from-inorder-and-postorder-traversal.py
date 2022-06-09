# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def construct(left, right):
            nonlocal i
            if left > right:
                return None
            root_val = postorder[i]
            i -= 1
            root_idx = cache[root_val]
            right_subtree = construct(root_idx + 1, right)
            left_subtree = construct(left, root_idx - 1)
            return TreeNode(root_val, left_subtree, right_subtree)
        
        cache = {}
        n = len(inorder)
        i = n - 1
        for j , val in enumerate(inorder):
            cache[val] = j
        return construct(0, n - 1)
            
        