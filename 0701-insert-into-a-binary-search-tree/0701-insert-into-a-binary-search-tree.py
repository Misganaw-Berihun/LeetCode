# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        cur = root
        
        while cur and cur.val != val:
            if cur.val > val:
                if not cur.left:
                    cur.left = newNode
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = newNode
                cur = cur.right
        
        return root or newNode
                
        
        