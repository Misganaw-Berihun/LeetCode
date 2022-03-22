class Solution {
    public boolean isPerfectSquare(int num) {
        long left = 1,right =(long) num;
        
        while (left <= right){
            long mid = left + (right - left) / 2;
            long sq = mid * mid;
           
            if (sq > num){
                right = mid - 1;
            }else if (sq < num){
                left = mid + 1;
            }else{
                return true;
            }
        }
        
        return false;
        
    }
}