# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        preorder = []
        
        if not root:
            return []
        
        stack.append(root)
        preorder.append(root.val)
        cur = root
        while stack:
            while cur.left:
                cur = cur.left
                preorder.append(cur.val)
                stack.append(cur)
            
            top = stack.pop()
            if top.right:
                cur = top.right
                stack.append(cur)
                preorder.append(cur.val)
    
        return preorder
            