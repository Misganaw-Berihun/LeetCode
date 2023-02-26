class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift = [0 for i in range(n)]
        ans = []
        
        for st, e, d in shifts:
            temp = 1
            if d == 0:
                temp *= -1
                
            shift[st] += temp
            if e + 1 < n:
                shift[e+1] -= temp
        
        for i in range(1, n):
            shift[i] += shift[i-1]
        
        for i in range(n):
            cur_shift = shift[i]
            temp = (cur_shift + ord(s[i]) - ord('a')) % 26 + ord('a')
            char = chr(temp)
            ans.append(char)
        
        return ''.join(ans)
        
        