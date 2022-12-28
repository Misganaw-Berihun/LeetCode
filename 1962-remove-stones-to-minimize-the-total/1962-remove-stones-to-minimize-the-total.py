class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        '''
            2  4  9          2 4 9
                             2 4 4
                             5 2 4
                             
            4 3 6 4      
            4 3 3 4      
            2 3 3 4
            
            2 + 6 + 4
        '''
        heap = []
        f = lambda a: -a
        
        for stones in piles:
            heappush(heap, -stones)
        
        while k > 0:
            top = -heappop(heap)
            half = (top + 1) // 2
            
            heappush(heap, -half)
            k -= 1
        
        return sum(map(f, heap))