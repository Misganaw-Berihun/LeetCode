class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(row,col):
            image[row][col] = newColor
            visited.add((row,col))
            
            for direction in DIR:
                newRow = row + direction[0]
                newCol = col + direction[1]
                
                if (newRow,newCol) in visited or not in_bound(newRow,newCol) or \
                            image[newRow][newCol] != color:
                    continue
                    
                dfs(newRow,newCol)
                
                
        visited = set()
        color = image[sr][sc]
        m = len(image)
        n = len(image[0])
        DIR = [[0,1],[0,-1],[1,0],[-1,0]]
        in_bound = lambda row,col : 0 <= row < m and 0 <= col < n
        dfs(sr,sc)
        
        return image
        
                
                    
                
                
                
                
                