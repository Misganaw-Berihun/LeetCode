# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(rt, level):
            if  rt:
                if self.max_level < level:
                    self.ans = rt.val
                    self.max_level = level
                left = dfs(rt.left ,level + 1)
                right = dfs(rt.right, level + 1)
        self.ans = root.val
        self.max_level = 0
        dfs(root,0)
        return self.ans
        