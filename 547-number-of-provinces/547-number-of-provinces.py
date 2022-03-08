class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i,j):
            visited.add((i,j))
            visited.add((j,i))
            for k in range(len(isConnected[i])):
                if (i,k) not in visited and isConnected[i][k] == 1:
                    dfs(k,i)
                 
        visited = set()
        provinces = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and (i,j) not in visited:
                    dfs(i,j)
                    provinces += 1
                
        return provinces
                
                    
                    
                    
                    
        
            