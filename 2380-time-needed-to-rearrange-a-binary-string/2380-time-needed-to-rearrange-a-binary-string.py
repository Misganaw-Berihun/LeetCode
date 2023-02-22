class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        arr = list(s)
        n = len(s)
        ans = 0
        
        exist = True
        while exist:
            exist = False
            copy = arr.copy()
            for i in range(1, n):
                if arr[i] == '1' and arr[i-1] == '0':
                    copy[i - 1] = '1'
                    copy[i] = '0'
                    exist = True
            
            if exist:
                ans += 1
            arr = copy.copy()
        return ans
            