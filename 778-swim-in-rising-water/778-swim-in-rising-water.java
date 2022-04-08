class Solution {
    private static boolean dfs(int[][] grid, int i, int j, int waterLevel, 
                               int[][] dir, int N, Set<Pair<Integer, Integer>> visited){
        visited.add(new Pair(i,j));
        for (int [] cur: dir){
            int neiR = cur[0] + i, neiC = cur[1] + j;
            
            if ( neiR >= 0 && neiR < N && neiC >= 0 && neiC < N 
                && !visited.contains(new Pair(neiR, neiC))
                && grid[neiR][neiC] <= waterLevel ){
                     if (neiR== N - 1 && neiC == N - 1){ return true;}
                    if (dfs(grid, neiR, neiC, waterLevel, dir, N, visited)) return true;
                   }
        }
        return false;
    }
    public int swimInWater(int[][] grid) {
        int N  =  grid.length, left  =  grid[0][0], right = N * N  -  1 ;
        final int [][] DIR = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
        
        while (left  <  right){
            int mid = left + (right - left) / 2;
            Set<Pair<Integer, Integer>> visited  =  new HashSet() ;
            
            if (dfs(grid, 0, 0,  mid,  DIR, N, visited)){
                    right = mid;
            }else{
                    left = mid + 1;
            }
        }
        return left;
    }
}