class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        length = len(s)
        def palindrome(string):
            i, j = 0, len(string) - 1
            ok = True
            
            while i < j and ok:
                if string[i] != string[j]:
                    ok = False
                
                i += 1
                j -= 1
                    
            return ok
            
        def backtrack(cur, path):
            if cur >= length:
                ans.append(path)
                return
            
            for i in range(cur + 1, length + 1):
                part = s[cur: i]
                if palindrome(part):
                    backtrack(i, path + [part])
        
        backtrack(0, [])
        return ans