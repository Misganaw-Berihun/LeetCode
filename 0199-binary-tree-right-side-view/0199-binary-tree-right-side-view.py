'''
Given the root of a binary tree, imagine yourself standing on the right side of it,
 return the values of the nodes you can see ordered from top to bottom.
 
 Input: root = [1,2,3,null,5,null,4]
 [5,4], ans = [1,3,4]
        1
    2      3
     5       4
     

Output: [1,3,4]

Input: root = [1,null,3]
Output: [1,3]

Input: root = []
Output: []
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        - traverse the binary tree
        - store the last element into an array at each level
        - returning the array
        """
        if not root:
            return []
        ans = [root.val]
        que = deque([root])
        while que :
            r = len(que)
            for i in range(r):
                temp = que.popleft()
                if temp.left:
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
            if que:
                ans.append(que[-1].val)
        return ans
            
             
        
        