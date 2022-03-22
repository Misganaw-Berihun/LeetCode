class Solution {
    public static int binarySearch(char [] letters,char target){
        int left = 0,n = letters.length ,right = n - 1;
        
        while (left <= right){
            int mid = left + (right - left) / 2;
            
            if (letters[mid] > target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        
        if (left == n ) return  0;
        
        return left;
    }
    public char nextGreatestLetter(char[] letters, char target) {
        return letters[binarySearch(letters,target)];     
    }
}