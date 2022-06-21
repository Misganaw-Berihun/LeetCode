class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colset, add, diff = set(), set(), set()
        ans = []
        def backtrack(i, comb):
            if (i >= n):
                ans.append(comb[:])
                return
            
            s = ['.' for k in range(n)]
            for c in range(n):
                if c not in colset and (i - c) not in diff and (i  + c) not in add:
                    colset.add(c)
                    add.add(c + i)
                    diff.add(i - c)
                    s[c] = 'Q';
                    comb.append(''.join(s))
                    backtrack(i + 1, comb[:])
                    s[c] = '.'
                    colset.remove(c)
                    add.remove(c + i)
                    diff.remove(i - c)
                    comb.pop()
                    
        backtrack(0, [])
        return ans
            
        