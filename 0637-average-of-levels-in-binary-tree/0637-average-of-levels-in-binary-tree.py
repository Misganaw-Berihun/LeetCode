# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root):
        queue = deque()
        queue.append(root)
        averages = []

        while queue:
            cur_level_count = len(queue)
            i = 0
            total = 0

            for i in range(cur_level_count):
                curr = queue.popleft() 
                total += curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            averages.append(total/cur_level_count)

        return averages
        
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:        
        return self.bfs(root)
                    
                
                    
                
                
                
                
                    
                
                
            
        
        