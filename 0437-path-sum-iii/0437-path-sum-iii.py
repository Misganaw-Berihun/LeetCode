# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(cur, count, tot):
            nonlocal ans
            if not cur:
                return
            tot += cur.val
            ans += count[tot - targetSum]
            count[tot] += 1
            dfs(cur.left, count, tot)
            dfs(cur.right, count,tot)
            count[tot] -= 1
        
        ans = 0
        dfs(root, Counter([0]), 0)
        return ans