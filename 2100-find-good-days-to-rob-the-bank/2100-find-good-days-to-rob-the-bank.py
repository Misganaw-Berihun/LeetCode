class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        inc_cnt = [0 for i in range(n)]
        dec_cnt = [0 for i in range(n)]
        ans = []
        
        for i in range(1,n):
            if security[i] <= security[i - 1]:
                dec_cnt[i] = 1 + dec_cnt[i - 1]
        
        for j in range(n - 2, -1, -1):
            if security[j] <= security[j + 1]:    
                inc_cnt[j] = inc_cnt[j + 1] + 1 
      
        for i in range(n):
            if inc_cnt[i] >= time and dec_cnt[i] >= time:
                ans.append(i)
                
        return ans
            
            
        