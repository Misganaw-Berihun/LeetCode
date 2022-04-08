class Solution:
    def in_bound(self,  r,  c, n):
        return 0 <= r < n and 0 <= c < n
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        n = len(grid)
        visited = set()
        
        neighbours = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        heappush(heap, (grid[0][0], 0, 0))
        visited.add((0,0))
        
        while heap:
            curMax , row, col =  heappop(heap)
            if row == n - 1 and col == n - 1:
                return curMax
            
            for i, j  in  neighbours:
                    new_row,  new_col = i + row,  j + col
                    if (not self.in_bound(new_row, new_col, n) or 
                                (new_row, new_col) in visited):
                            continue
                    visited.add((new_row, new_col))
                    heappush(heap, ( max(curMax, grid[new_row][new_col]) ,  new_row,  new_col))
            
                        
                    
                    
                    
            
            
            
        
                            
                            
            
                            
                
                        

                    
                         
                        
                
                            
                    
                    
                
                
        