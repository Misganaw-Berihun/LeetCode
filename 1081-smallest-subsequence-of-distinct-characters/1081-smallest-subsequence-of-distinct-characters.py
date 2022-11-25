class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stk, last_idx, ans = [], defaultdict(int), ""
        visited = set()
        
        for i in range(len(s)):
            last_idx[s[i]] = i
            
        for i in range(len(s)):
            while stk and s[i] not in visited and \
                        stk[-1] >= s[i] and i < last_idx[stk[-1]]:
                visited.remove(stk.pop())
            
            if s[i] not in visited:
                stk.append(s[i])
                visited.add(s[i])
                
        while stk:
            ans = stk.pop()   + ans
        
        return ans