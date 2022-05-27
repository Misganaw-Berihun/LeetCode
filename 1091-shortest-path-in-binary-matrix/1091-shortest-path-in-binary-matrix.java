class Solution {
    private static boolean inBound(int i , int j, int n, int m){
        return 0 <= i &&  0 <= j && i < n && j < m;
    }
    public int shortestPathBinaryMatrix(int[][] grid) {
        if (grid[0][0] == 1) return -1;
        ArrayDeque<int []> queue = new ArrayDeque();
        int n = grid.length, m = grid[0].length;
        Set<String> visited = new HashSet();
        int ans = 0;
        int [][] dir = {{-1, 0}, {1, 0}, {-1, -1}, {0, -1}, {0, 1} ,{1, -1}, {-1, 1}, {1, 1}};
        queue.addLast(new int[]{0, 0});
        visited.add("0,0");
        while (!queue.isEmpty()){
            int o = queue.size();
            ans++;
            for (int i  = 0; i < o; i++){
                int []cur = queue.pollFirst();
                if ( cur[0] == n - 1 && cur[1] == n - 1){
                    return ans;
                }
                for (int []d: dir){
                    int r = d[0] + cur[0], c = d[1] + cur[1];
                    if (inBound(r, c, n, m) && !visited.contains(r +"," + c) && grid[r][c] == 0){
                        visited.add(r + "," + c);
                        queue.addLast(new int[]{r, c});
                    }
                }
            }
        }
        return  -1;
    }
}