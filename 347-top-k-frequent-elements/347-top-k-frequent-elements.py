class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        fre_val = []
        tr = k
        
        for i,v in freq.items():
            if tr > 0:
                fre_val.append((v,i))
                tr -= 1
            elif tr == 0:
                heapq.heapify(fre_val)
                tr = -1
            
            if tr == -1:
                heapq.heappush(fre_val,(v,i))
                heapq.heappop(fre_val)
            
        return list(map(lambda a: a[1] ,fre_val))
                
                
            
                
            
        