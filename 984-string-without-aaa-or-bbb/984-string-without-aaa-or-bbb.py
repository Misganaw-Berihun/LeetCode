class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        cur = ord('a')
        tot = ord('a') + ord('b')
        
        if a < b:
            cur = tot - cur
            
        while a > 0 and b > 0 and abs(a - b) > 1:
            ans.append(chr(cur))
            ans.append(chr(cur))
            ans.append(chr(tot - cur))
            a -= 1
            b -= 1
            if chr(cur) == 'a':
                a -= 1
            else:
                b -= 1
                
        while a > 0 and b > 0:           
            ans.append(chr(cur))
            ans.append(chr(tot - cur))
            a -= 1
            b -= 1
        
        while a > 0:
            ans.append('a')
            a -= 1
        
        while b > 0:
            ans.append('b')
            b -= 1
        
        return ''.join(ans)
        