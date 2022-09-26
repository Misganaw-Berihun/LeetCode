class Solution:
    def minWindow(self, s: str, t: str) -> str:
        vis = defaultdict(int)
        req = defaultdict(int)
        start, end, cnt, j, l = 0, -1, 0, 0, float('inf')
        
        for ch in t:
            req[ch] += 1
        
        for i in range(len(s)):
            ch = s[i]
            if (req[ch] > 0):
                vis[ch] += 1
                if vis[ch] <= req[ch]:   
                    cnt += 1
                    
            while cnt == len(t) and j < len(s) and j <= i:
                if (i - j + 1) < l:
                    start, end = j, i
                    l = end - start + 1
    
                c = s[j] 
                if req[c] > 0:
                    vis[c] -= 1
                    if vis[c] < req[c]:
                        cnt -= 1
                j += 1
        return s[start: end + 1]
                
                
            
            
                
            
            
        
        