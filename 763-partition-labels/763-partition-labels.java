class Solution {
    public List<Integer> partitionLabels(String s) {
        int n = s.length();
        List<Integer> partitions = new ArrayList<Integer>();
        int rightEnd = 0, leftEnd = 0;
        Map<Character, Integer> lastOccurence = new HashMap<Character, Integer>();
        for (int i = 0; i < n; i++){
            lastOccurence.put(s.charAt(i), i);
        }
        
        for (int j = 0; j < n; j++){
            rightEnd = Math.max(rightEnd, lastOccurence.get(s.charAt(j)));
            if (j == rightEnd){
                partitions.add(rightEnd - leftEnd + 1);
                leftEnd = j + 1;
            }
        }
        return partitions;
    }
}