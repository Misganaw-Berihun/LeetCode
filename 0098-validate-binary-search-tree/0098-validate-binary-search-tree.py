# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(curNode, curMax, curMin):
            if not curNode:
                return True
            
            if not (curMin < curNode.val < curMax):
                return False
            
            if not isValid(curNode.left, curNode.val, curMin):
                return False
            
            if not isValid(curNode.right, curMax, curNode.val):
                return False
            
            return True
        
        return isValid(root, float('inf'), float('-inf'))
            
        