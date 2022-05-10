class Solution
{
    private static boolean canBe(String[] strs, int limit)
    {
            String pre = strs[0].substring(0, limit);
            for (int i = 1;  i < strs.length; ++i)
            {
                    if (!strs[i].startsWith(pre))
                    {
                            return false;
                    }
            }
            return true; 
    }
    
   public String longestCommonPrefix(String[] strs) 
   {
            if (strs == null || strs.length == 0) return "";
            if  (strs.length == 1) return strs[0];
            int minLen = Integer.MAX_VALUE;
            for (int i = 0; i < strs.length; i++)
            {
                    minLen = Math.min(minLen, strs[i].length());
            }
            int left = 0, right = minLen;
            while (left < right)
            {
                    int mid = left + (right - left  + 1) / 2;
                    if  (canBe(strs, mid))
                    {
                            left = mid;
                    }
                    else
                    {
                            right = mid - 1;
                    }
            }
            return strs[0].substring(0, left);   
    }
}