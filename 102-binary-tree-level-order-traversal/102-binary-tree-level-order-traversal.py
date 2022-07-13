# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ret = []
        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue)
            temp = []
            for i in range(n):
                cur = queue.popleft()
                temp.append(cur.val)
                if cur.left:    
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ret.append(temp)
        return ret