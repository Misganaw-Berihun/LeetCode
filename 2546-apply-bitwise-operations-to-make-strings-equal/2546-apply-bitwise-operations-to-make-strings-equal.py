class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        cnt1 = s.count('1')
        cnt2 = target.count('1')
        
        ans = True
        if cnt1 == 0 and cnt2 != 0:
            ans = False
        elif cnt1 != 0 and cnt2 == 0:
            ans = False
        
        return ans
        