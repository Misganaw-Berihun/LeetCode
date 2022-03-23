class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        int [] visited = new int[1001];
        Arrays.fill(visited,-1);
        List<Integer> ans = new ArrayList<Integer>();
        
        for(int num:nums1){
            visited[num] = 1;
        }
        
        for(int num: nums2){
            if (visited[num] >= 0){
                visited[num] = 0;
            }
        }
        
        for(int num: nums1){
            if(visited[num] != 0){
                visited[num] = -1;
            }
        }
        
        for(int num :nums2){
            if(visited[num] != 0){
                visited[num] = -1;
            }
        }
        
        for(int i = 0; i < 1001; i++){
            if(visited[i] == 0){
                ans.add(i);
            }
        }
        
        return ans.stream().mapToInt(i -> i).toArray();
    }
}