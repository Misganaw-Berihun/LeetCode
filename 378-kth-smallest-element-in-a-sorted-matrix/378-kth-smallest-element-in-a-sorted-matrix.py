class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        ans = 0
        n = len(matrix)
        m = len(matrix[0])
               
        for i in range(len(matrix[0])):
            heapq.heappush(heap,(matrix[0][i],0,i))
                           
        for i in range(k,0,-1):
            ans = heapq.heappop(heap)
            p = ans[1] + 1
            q = ans[2]
            if p < m:
                val = matrix[p][ans[2]] 
                heapq.heappush(heap,(val,p,q))
                
        return ans[0]
            
        
        