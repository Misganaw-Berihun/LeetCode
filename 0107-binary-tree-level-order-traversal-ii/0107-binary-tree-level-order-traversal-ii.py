# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def levelOrder(cur, level, order):
            if not cur:
                return
            
            if len(order) == level:
                order.append([cur.val])
            
            else:
                order[level].append(cur.val)
            
            levelOrder(cur.left, level + 1, order)
            levelOrder(cur.right, level + 1, order)
        
        order = []
        levelOrder(root, 0, order)
        return order[::-1]