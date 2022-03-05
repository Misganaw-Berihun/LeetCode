class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        fre_val = []
        ans = []
        
        for i,v in count.items():
            fre_val.append((-v,i))
      
        heapq.heapify(fre_val)
    
        while k > 0:
            ans.append(heapq.heappop(fre_val)[1])
            k -= 1
        
        return ans 