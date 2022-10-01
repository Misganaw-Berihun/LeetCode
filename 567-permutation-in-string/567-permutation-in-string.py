class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = Counter(s1)
        n, m = len(s2), len(s1)
        
        for i in range(n - m + 1):
            cnt2 = Counter(s2[i: i + m])
            poss = True
            for k, v in cnt2.items():
                if k not in cnt1 or cnt2[k] != cnt1[k]:
                    poss = False
            
            if poss: 
                return poss
                
        return False
                
        
        