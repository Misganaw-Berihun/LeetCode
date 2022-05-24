"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        pre = root
        while pre != None:
            cur = pre
            while cur and cur.left:
                cur.left.next = cur.right
                cur.right.next = None if not cur.next else cur.next.left
                cur = cur.next
            pre = pre.left
        return root
        