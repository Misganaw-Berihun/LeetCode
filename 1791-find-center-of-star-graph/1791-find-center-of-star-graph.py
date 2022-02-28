class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        int1 = edges[0][0]
        int2 = edges[0][1]
        
        for i in range(1,len(edges)):
            [a,b] = edges[i]
            
            if int1 == a or int1 == b:
                int2 = -1
            else:
                int1 = -1
            
        
        if int1 != -1:
            return int1
        else:
            return int2
            
        
        