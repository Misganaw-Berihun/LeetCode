# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaf(self, cur, leavies):
        if not cur:
            return True
        
        left = self.findLeaf(cur.left, leavies)
        right = self.findLeaf(cur.right, leavies)
        
        if left and right:
            leavies.append(cur.val)
        return False
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leavies_1 = []
        leavies_2 = []
        self.findLeaf(root1, leavies_1)
        self.findLeaf(root2, leavies_2)
        
        return leavies_1 == leavies_2
        