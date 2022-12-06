class Solution:
    def backtrack(self,cookies, share, cur, N, ans):
        if cur >= N:
            mx = -inf
            for i in range(len(share)):
                mx = max(share[i], mx)
            ans[0] = min(ans[0], mx)
            return
        
        for i in range(len(share)):
            share[i] += cookies[cur]
            self.backtrack(cookies, share, cur + 1, N , ans)
            share[i] -= cookies[cur]
            if share[i] == 0:
                break
            
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        share = [0 for i in range(k)]
        N = len(cookies)
        ans = [inf]
        self.backtrack(cookies, share, 0, N, ans)
        return ans[0]
        
        