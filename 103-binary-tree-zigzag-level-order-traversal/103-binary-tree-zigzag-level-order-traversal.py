# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(rt):
            if not rt:
                return
            
            queue = deque()
            queue.append(rt)
            level = -1
            ret = []
            
            while queue:
                n = len(queue)
                level += 1
                temp = []
                
                for i in range(n):
                    cur = queue.popleft()
                    temp.append(cur.val)
                
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                
                if level % 2 == 1:
                    ret.append(temp[::-1])
                else:
                    ret.append(temp)
                    
            return ret
        
        return bfs(root)
                        
                    
                        
                    
                
                
                
        