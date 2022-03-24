# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque()
        ans = []
        queue.append(root)
        
        while queue:
            n = len(queue)
            largest = float('-inf')
            
            for i in range(n):
                cur = queue.popleft()
                if cur.val > largest:
                    largest = cur.val
                    
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                    
            ans.append(largest)
        return ans
        
            
            
            
           
    
        
        