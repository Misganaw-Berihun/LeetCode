class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        max_starting_x = max(ax1, bx1)
        max_ending_x = min(ax2, bx2)
        max_starting_y = max(ay1, by1)
        max_ending_y = min(ay2, by2)
        
        area1 = abs(ax2 - ax1) * abs(ay1 - ay2)
        area2 = abs(bx2 - bx1) * abs(by1 - by2)
        
        val1, val2 = max(0, max_ending_x - max_starting_x),  max(0, max_ending_y - max_starting_y)
        rem = val1 * val2
        ret = area1 + area2 - rem
        return ret
        