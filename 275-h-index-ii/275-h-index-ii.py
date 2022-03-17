class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def bsa(val):
            l = 0
            n = len(citations)
            r = n - 1

            while l <= r:
                m = l + (r - l) // 2
                
                if citations[m] < val :
                    l = m + 1
                else:
                    r = m - 1
                    
            return l
        
        l = 0
        n = len(citations)
        r = n 
        ans= 0
        
        while l <= r:
            m = l + (r-l) // 2
            k = bsa(m)
            
            if m <= n - k:
                l = m + 1
            else:
                r = m - 1
                
        return l - 1