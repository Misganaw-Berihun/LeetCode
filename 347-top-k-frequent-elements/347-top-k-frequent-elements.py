class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        fre_val = []
        
        for i,v in freq.items():
            if k>0:
                heapq.heappush(fre_val,(v,i))
                k -= 1
            
            elif k == 0:
                heapq.heappushpop(fre_val,(v,i))
            
        return list(map(lambda a: a[1] ,fre_val))
                
                
            
                
            
        