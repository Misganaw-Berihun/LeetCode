class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        interval_dict = defaultdict(list)
        ans = []
        
        for i,ch in enumerate(s):
            temp  = interval_dict.get(ch)
            if temp == None:
                interval_dict[ch] = [i,i]
            else:
                interval_dict[ch][1] = i
            
        interval = list(interval_dict.values())
        start,end = interval[0][0],interval[0][1]
        
        for i in range(1,len(interval)):
            if interval[i][0] <= end:
                end = max(interval[i][1],end)
            else:
                ans.append(end - start + 1)
                start = interval[i][0]
                end = interval[i][1]
                
        ans.append(end - start + 1)
        return ans
                
                
            
        
                
        
            
            
     
            
        
        
        
        
                
                
                
            
        
        