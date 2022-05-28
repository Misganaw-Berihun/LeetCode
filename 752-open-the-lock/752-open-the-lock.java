class Solution {
    public int openLock(String[] deadends, String target) {
        int ans = 0;
        Set<String> begin = new HashSet();
        Set<String> end = new HashSet();
        Set<String> deadSet = new HashSet(Arrays.asList(deadends));
        Set<String> temp;
        begin.add("0000");
        end.add(target);
        while (!begin.isEmpty() || !end.isEmpty()){
            if (begin.size() < end.size()){
                temp = begin;
                begin = end;
                end = temp;
            }
            temp = new HashSet();
            for (String s: begin){
                if (end.contains(s)) return ans;
                if (deadSet.contains(s)) continue;
                deadSet.add(s);
                
                StringBuilder sb = new StringBuilder(s);
                for (int i = 0; i < 4; i++){
                    char ch = s.charAt(i);
                    String s1 = sb.substring(0 , i)  +  (ch == '9'? 0 : ch - '0' + 1) + sb.substring(i + 1);
                    String s2 = sb.substring(0,  i)  +  (ch == '0' ? 9: ch - '0'  - 1) + sb.substring(i + 1);
                    
                    if (!deadSet.contains(s1))
                        temp.add(s1);
                    if (!deadSet.contains(s2))
                        temp.add(s2);
                }
            }
            begin = end;
            end = temp;
            ans ++;
        }
        return -1;
    }
}