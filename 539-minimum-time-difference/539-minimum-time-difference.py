class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ans = float('inf')
        timePoints.sort()
        zipped = list(zip(timePoints,timePoints[1:] + [timePoints[0]]))
        for t1, t2 in zipped:
            min1 = 60 * int(t1[:2]) + int(t1[3:])
            min2 = 60 * int(t2[:2]) + int(t2[3:])
            ans = min(abs(min1 - min2), ans)
        l = zipped[-1]
        ans = min(ans, abs((60 * (24 + int(l[1][:2])) + int(l[1][3:])) - (60 * int(l[0][:2]) + int(l[0][3:])) ))
        return ans
            
        
        