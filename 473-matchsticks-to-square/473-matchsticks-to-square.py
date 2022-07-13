class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        @cache
        def dp(i, g1, g2, g3, g4):
            if i < 0:
                if g1 == g2 == g3 == g4:
                    return True
                return False
            
            if g1 > side or g2 > side or g3 > side or g4 > side:
                return False
            
            if dp(i - 1, g1 + matchsticks[i], g2, g3, g4):
                return True
            if dp(i - 1, g1, g2 + matchsticks[i], g3, g4):
                return True
            if dp(i - 1, g1, g2, g3 + matchsticks[i], g4):
                return True
            if dp(i - 1, g1, g2, g3, g4 + matchsticks[i]):
                return True
            
        n = len(matchsticks)
        perim = sum(matchsticks)
        if perim % 4 != 0:
            return False
        side = perim / 4
        matchsticks.sort()
        return dp(n - 1, 0, 0, 0, 0)
            
        