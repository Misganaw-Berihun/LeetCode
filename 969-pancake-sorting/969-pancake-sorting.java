class Solution {
    private static void reverse(int [] arr, int range)
    {
        int i = 0, j = range;
        while (i <= j){
            int temp = arr[i];
            arr[i++] = arr[j];
            arr[j--] = temp;
        }
    }
    public List<Integer> pancakeSort(int[] arr)
    {
        int n = arr.length;
        List <Integer>  ans = new ArrayList<> ();
    
        for( int i = n - 1 ;  i >= 0 ;  --i )
        {
            int maxIdx = 0;
            for( int j = 1 ;  j <= i ; ++j )
            {
                maxIdx = (arr[j] > arr[maxIdx])? j : maxIdx;
            }
            if (maxIdx == i) 
            {
                continue;
            }
            if (maxIdx != 0) 
            {
                    reverse(arr, maxIdx);
                    ans.add(maxIdx + 1);
            }
            reverse(arr, i);
            ans.add(i + 1);
            }
            return ans;
    }
}