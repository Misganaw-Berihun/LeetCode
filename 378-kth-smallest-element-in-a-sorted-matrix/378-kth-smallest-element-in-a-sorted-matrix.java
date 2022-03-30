class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length; 
        int left = matrix[0][0], right = matrix[n-1][n-1];
        
        while (left < right){
            int count = 0;
            int mid = left + (right - left ) / 2;
            int j = n - 1;
            for (int i = 0; i < n; i++){
                while (j >= 0 && matrix[i][j] > mid) j--;
                count +=  (j + 1);
            }
            
            if (count >= k) right = mid;
            else left = mid + 1;
        }
        return left;
    }
}