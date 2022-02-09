class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue =  deque()
        res = inf
        
        #Create a prefix sum array for nums
        prefix = [0]*(len(nums)+1)
        for ind, i in enumerate(nums, 1):
            prefix[ind] = prefix[ind-1] + i
        
        #Simulate two pointer approach using montonic queue
        for ind, i in enumerate(prefix):
            #To make every item in the queue increasing
            while queue and i<=prefix[queue[-1]]:
                queue.pop()

            #To find the minimum satisfying window
            while queue and i - prefix[queue[0]] >= k:
                left = queue.popleft()
                res = min(res, ind - left)    
                
            queue.append(ind)
        return res if res!=inf else -1
        