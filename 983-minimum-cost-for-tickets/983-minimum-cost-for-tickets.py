class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def dp(idx):
            if idx in memo:
                return memo[idx]
            if idx >= len(days):
                return 0
            
            memo[idx] = min(
                dp(bisect.bisect_left(days,days[idx] + 1)) + costs[0],
                dp(bisect.bisect_left(days,days[idx]+ 7)) + costs[1],
                dp(bisect.bisect_left(days,days[idx]+ 30)) + costs[2]
            )
            
            return memo[idx]
        
        return dp(0)