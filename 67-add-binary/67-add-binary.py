class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c, n, m = 0, len(a), len(b)
        i, j = n - 1, m - 1
        ans = []
    
        while i >= 0 or j >= 0:
            d, e = '0', '0'
            if i >= 0:
                d = a[i]
            if j >= 0:
                e = b[j]
            d , e = int(d), int(e)
            res = d ^ e ^ c
            c = (e & d) | (c & e) | (c & d)
            ans.append(str(res ))
            i -= 1
            j -= 1
        
        if c == 1:
            ans.append(str(c))
        return ''.join(ans[::-1])
            