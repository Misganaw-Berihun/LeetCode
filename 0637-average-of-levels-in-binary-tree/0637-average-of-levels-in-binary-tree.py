# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:        
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # initialize an empty list to store the averages
        averages = []
        # check if the root node is None
        if root is None:
            return averages
        # create a queue and add the root node
        queue = deque([root])
        # loop until the queue is empty
        while queue:
            # get the number of nodes in the current level
            level_size = len(queue)
            # initialize variables for sum and count of nodes
            level_sum = 0
            count = 0
            # loop through all the nodes in the current level
            for i in range(level_size):
                # remove the first node from the queue
                node = queue.popleft()
                # add the node's value to the level sum
                level_sum += node.val
                # increment the count of nodes
                count += 1
                # add the node's children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # calculate the average for the current level and append to the averages list
            averages.append(level_sum / count)
        # return the averages list
        return averages




                
                
                
                
                    
                
                
            
        
        