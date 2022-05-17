# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        level = 0
        queue.append(root)
        
        while queue:
            n = len(queue)
            level += 1
            
            for i in range(n):
                cur = queue.popleft()
                if not cur.left and not cur.right:
                    return level
                if cur.left:    
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                
        return level
            
        