class Solution {
    public int numRescueBoats(int[] people, int limit) {
        int num_boats = 0,n = people.length;
        int left_ptr = 0,right_ptr = n - 1;
        Arrays.sort(people);
        
        while(left_ptr <= right_ptr){
            int weight = people[left_ptr] + people[right_ptr];
            
            if(weight <= limit){
                    left_ptr++;
                }
                num_boats++;
                right_ptr--;
        }
        return num_boats;
    }
}