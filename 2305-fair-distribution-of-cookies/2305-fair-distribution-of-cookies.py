class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def dp(idx, k_child):
            nonlocal min_unfairness
            if idx >= len(cookies):
                min_unfairness = min(min_unfairness, max(k_child))
                return 

            if max(k_child) >= min_unfairness:
                return 
            
            for i in range(len(k_child)):
                k_child[i] += cookies[idx]
                dp(idx + 1, k_child)
                k_child[i] -= cookies[idx]

        min_unfairness = float('inf')
        cookies.sort(reverse = True)
        dp(0, [0 for _ in range(k)])
        return min_unfairness
       
        
        