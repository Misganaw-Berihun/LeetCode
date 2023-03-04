class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #[3,9,20,null,null,15,7]
        if not root:
            return []
        result = []
        queue = deque([root])
        level = 0
        
        while queue:
            size = len(queue)
            temp = []
            
            for _ in range(size):
                curr_node = queue.popleft()
                temp.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            if level % 2 != 0:
                temp = temp[::-1]
            result.append(temp)
            level += 1 
        return result
            