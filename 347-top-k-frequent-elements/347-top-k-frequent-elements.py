class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        fre_val = []
        
        for i,v in freq.items():
            heapq.heappush(fre_val,(v,i))
            k -= 1
            
            if k < 0:
                heapq.heappop(fre_val)
            
        return list(map(lambda a: a[1] ,fre_val))
                
                
            
                
            
        