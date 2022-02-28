class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        c,d = edges[0]
        a,b = edges[1]
        
        if c == a or c == b:
            return c
        else:
            return d

        
            
        
        