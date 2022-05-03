public class LengthFirstComparator implements Comparator<String> {
    public int compare(String o1, String o2) {             
        if (o1.length()!=o2.length()) {
            return o1.length()-o2.length(); 
        }
        return o1.compareTo(o2);
    }
}
class Solution {
    public String kthLargestNumber(String[] nums, int k) {
           Arrays.sort(nums, new LengthFirstComparator());
            return nums[nums.length - k];
        }
}