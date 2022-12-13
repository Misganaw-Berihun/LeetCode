class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        const int ROWS = matrix.size();
        const int COLS = matrix[0].size();
        
        vector<int> moves = {1, 0, -1};
        vector<int> curRow(COLS, 0);
        
        for (int row = 0; row < ROWS ; row++){
            vector<int> newRow(COLS, 0);
            for (int col = 0; col < COLS; col++){
                int mn = INT_MAX;
                for (int dy: moves){
                    int ny = col + dy;
                    if (ny >= 0 && ny < COLS){
                        mn = min(mn, curRow[ny] + matrix[row][col]);
                    }
                }
                newRow[col] = mn;
            }
            curRow = newRow;
        }
        int ans = INT_MAX;
        for (int i = 0; i < COLS; i++){
            ans = min(ans, curRow[i]);
        }
        return ans;
    }
};