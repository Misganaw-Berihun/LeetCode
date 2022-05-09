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
    
    private static int maxUpTo(int [] arr, int range)
    {
        int maxIdx = 0;
        for( int j = 1 ;  j <= range ; ++j )
            {
                 maxIdx = (arr[j] > arr[maxIdx])? j : maxIdx;
            }
        return maxIdx;
    }
    
    public List<Integer> pancakeSort(int[] arr)
    {
        int n = arr.length;
        List <Integer>  ans = new ArrayList<> ();
    
        for( int i = n - 1 ;  i >= 0 ;  --i )
        {
            int maxIdx = maxUpTo(arr, i);
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