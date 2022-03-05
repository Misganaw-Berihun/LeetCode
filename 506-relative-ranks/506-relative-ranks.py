class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [""]*len(score)
        
        for i in range(len(score)):
            score[i] = [-score[i],i]
            
        heapq.heapify(score)
        
        for i in range(len(score)):
            v = heappop(score)
            if i == 0:
                ans[v[1]] = "Gold Medal"
            elif i == 1:
                ans[v[1]] = "Silver Medal"
            elif i == 2:
                ans[v[1]] = "Bronze Medal"
            else:
                ans[v[1]] = str(i + 1)
            
        return ans
                
                
            
        