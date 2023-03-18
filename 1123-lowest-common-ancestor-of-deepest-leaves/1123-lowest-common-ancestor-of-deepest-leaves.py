class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        deepest_leaves = []
        max_depth = 0

        def dfs(node, depth):
            nonlocal deepest_leaves, max_depth
            if not node:
                return 0

            left_depth = dfs(node.left, depth + 1)
            right_depth = dfs(node.right, depth + 1)

            if left_depth == right_depth and left_depth + depth >= max_depth:
                if left_depth + depth > max_depth:
                    deepest_leaves = []
                max_depth = left_depth + depth
                deepest_leaves.append(node)

            return max(left_depth, right_depth) + 1


        def find_lca(node, depth):
            if not node or depth == max_depth:
                return node, depth

            left_lca, left_depth = find_lca(node.left, depth + 1)
            right_lca, right_depth = find_lca(node.right, depth + 1)

            if left_lca and right_lca:
                return node, depth
            elif left_lca:
                return left_lca, left_depth
            else:
                return right_lca, right_depth
        
        dfs(root, 0)
        return find_lca(root, 0)[0]