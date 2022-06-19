class Solution {
    public int[][] highestPeak(int[][] isWater) {
        int n = isWater.length, m = isWater[0].length;
        ArrayDeque<int []> queue = new ArrayDeque<int []> ();
        int [][] heights = new int[n][m];
        for (int i = 0; i < n; i++){
            Arrays.fill(heights[i], -1);
        }
        final int [][] direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        for (int i = 0; i < n; i++){
            for (int j  = 0; j < m; j++){
                if (isWater[i][j] == 1){
                    queue.addLast(new int[]{i, j});
                    heights[i][j] = 0;
                }
            }
        }
        while (queue.size() > 0){
            int k = queue.size();
            
            for (int i = 0; i < k; i++){
                int [] cur = queue.pollFirst();
                
                for (int [] d : direction){
                    int r = cur[0] + d[0], c = cur[1] + d[1];
                    if (r < 0 || r >= n || c < 0 || c >=m || heights[r][c] != -1)
                        continue;
                    heights[r][c] = heights[cur[0]][cur[1]] + 1;
                    queue.addLast(new int[]{r, c});
                     }
            }
        }
        return heights;
    }
}