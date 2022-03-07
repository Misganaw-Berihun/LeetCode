class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        usedLadders = []
        n = len(heights)
        
        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            
            if diff <= 0:
                continue
            
            elif ladders > 0:
                ladders -= 1
                heappush(usedLadders,diff)
            
            elif usedLadders and diff > usedLadders[0] and bricks >= usedLadders[0]:
                bricks -= usedLadders[0]
                heappop(usedLadders)
                heappush(usedLadders,diff)
            
            elif bricks >= diff:
                bricks -= diff
            
            else:
                return i
            
                
        return n - 1
                
                
        
        
