class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(cur, path):
            if (cur == len(s)):
                ans.append(''.join(path))
                return
            
            backtrack(cur + 1, path + [s[cur]])
            if s[cur].isalpha():
                change_case = ''
                if s[cur].isupper():
                    change_case = s[cur].lower()
                else:
                    change_case = s[cur].upper()
                
                
                backtrack(cur + 1, path + [change_case])
        ans = []
        backtrack(0, [])
        return ans