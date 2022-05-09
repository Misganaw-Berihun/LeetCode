class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ans = float('inf')
        timePoints.sort()
        zipped = list(zip(timePoints,timePoints[1:] + [timePoints[0]]))
        for t1, t2 in zipped:
            a, b = t1.split(":")
            c, d = t2.split(":")
            min1 = 60 * int(a) + int(b)
            min2 = 60 * int(c) + int(d)
            ans = min(abs(min1 - min2), ans)
        a, b = zipped[-1][1].split(':')
        c, d = zipped[-1][0].split(':')
        ans = min(ans, abs((60 * (24 + int(a)) + int(b)) - (60 * int(c) + int(d)) ))
        return ans
            
        
        