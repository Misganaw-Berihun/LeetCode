class Solution {
    public int openLock(String[] deadends, String target) {
        Set <String> deadset = new HashSet();
        Set <String> visited = new HashSet();
        int ans = 0;
        ArrayDeque<String> queue = new ArrayDeque();
        queue.addLast("0000");
        visited.add("0000");
        
        for (String deadend : deadends){
            deadset.add(deadend);
        }
        if (deadset.contains("0000")){
            return -1;
        }
        while (!queue.isEmpty()){
            int n = queue.size();
            ans++;
            
            for(int i = 0; i < n ; i++){
                StringBuilder current = new StringBuilder(queue.pollFirst());
                if (current.toString().equals(target)){
                    return ans - 1;
                }
                for (int k = 0 ; k < 4; k++){
                    char ch = current.charAt(k);
                    String build = current.substring(0, k) + ( ch == '9' ? 0 :  ch - '0' + 1)  + current.substring(k + 1);
                    if (!deadset.contains(build) && !visited.contains(build)){
                        queue.addLast(build);
                        visited.add(build);
                    }
                    build = current.substring(0, k) + ( ch == '0' ? 9 :  (ch - '0' - 1)) + current.substring(k + 1);
                    if (!deadset.contains(build) && !visited.contains(build)){
                        queue.addLast(build);
                        visited.add(build);
                    }
                }
            }
        }
        return -1;
    }
}