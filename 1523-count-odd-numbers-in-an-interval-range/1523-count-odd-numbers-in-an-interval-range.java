class Solution {
    public int countOdds(int low, int high) {
        int odd;
        
        if ((high & 1) == 1 && (low & 1) == 1){
            odd =  high != low ? 
                    (high - low - 1) / 2 + 2:
                    1 ;
            
        }else if ((high & 1) == 0 && (low & 1) == 0){
            odd = (high - low) / 2 ;
        }else{
            odd = (high - low) / 2 + 1;
        }
        
        return odd;
    }
}