# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def bfs(rt):
            queue = deque()
            queue.append(rt)
            ret = []
            
            while queue:
                n = len(queue)
                i = 0
                total = 0
            
                while i < n:
                    curr = queue.popleft() 
                    total += curr.val
                    
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                        
                    i += 1
                ret.append(total/n)
                
            return ret
        
        return bfs(root)
                    
                
                    
                
                
                
                
                    
                
                
            
        
        