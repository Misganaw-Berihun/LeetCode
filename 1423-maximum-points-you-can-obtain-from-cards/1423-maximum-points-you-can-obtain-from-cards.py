class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
       # bacward = [12, 7,  1]
        n = len(cardPoints)
        backward = sum(cardPoints[-k:])
        forward = 0
        ans = backward
       
        
        for i in range(k):
            forward += cardPoints[i]
            backward -= (cardPoints[n - k + i])
            ans = max(ans, forward + backward)
        
        return ans
       
        
        