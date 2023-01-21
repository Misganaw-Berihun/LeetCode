class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        size = len(s)
        ans = set()
        def backtrack(cur, path):
            if cur >= size:
                if len(path) == 4:
                    ans.add('.'.join(path))
                return
            
            for j in range(1, 4):
                num = s[cur: cur + j]
                if (j > 1 and num[0] == '0'):
                    continue

                num_int = int(num)
                if 0 <= num_int < 256:
                    backtrack(cur + j, path + [num])
        
        backtrack(0, [])
        return ans
                
        