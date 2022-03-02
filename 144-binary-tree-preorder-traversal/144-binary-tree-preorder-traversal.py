# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        cur = root
        
        while True:
            
            if cur != None:
                ans.append(cur.val)
                stack.append(cur)
                cur = cur.left
                
            elif stack:
                cur = stack.pop().right
                
            else:
                break
                
        return ans