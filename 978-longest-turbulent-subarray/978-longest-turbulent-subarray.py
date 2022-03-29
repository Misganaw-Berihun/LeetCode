class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def cmp(a,b):
            return (a > b) - (a < b)
        ans = 1
        pin = 0
        
        for i in range(1,len(arr)):
            c = cmp(arr[i-1],arr[i])
            if c ==0:
                pin = i
            elif i == len(arr) - 1 or c * cmp(arr[i],arr[i+1]) != -1:
                ans = max(ans, i - pin + 1)
                pin = i
                
        return ans
                
            
            
            
            
        