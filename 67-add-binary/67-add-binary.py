class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c, n, m = 0, len(a), len(b)
        i, j = n - 1, m - 1
        ans = []
    
        while i >= 0 and j >= 0:
            d, e = int(a[i]), int(b[j])
            res = c ^ (e ^ d)
            c = (e & d) | (c & e) | (c & d)
            ans.append(str(res ))
            i -= 1
            j -= 1
        
        while i  >= 0:
            d = int(a[i])
            res = d ^ c
            c = (c & d)
            ans.append(str(res))
            i -= 1
        
        while j >= 0:
            e = int(b[j])
            res = e ^ c
            c = (c & e)
            ans.append(str(res))
            j -= 1
        if c == 1:
            ans.append(str(c))
        return ''.join(ans[::-1])
            