"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.visited = set()
        self.longest = 0
        
    def maxDepth(self, root: 'Node') -> int:
        def traverse(rt,level):
            self.visited.add(rt)
            level += 1

            for child in rt.children:
                if child not in self.visited:  
                    traverse(child,level)

            self.longest = max(self.longest,level)
            return self.longest
            
        self.longest = 0
        
        if not root:
            return 0
        return traverse(root,0)

        
                