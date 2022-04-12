class Solution {
    public String removeDuplicateLetters(String s) {
        if (s.length() == 0) return "";
        HashMap<Character, Integer> count = new HashMap<>();
        int pos = 0;
        
        for(int i = 0; i < s.length(); ++i){
            count.put(s.charAt(i), count.getOrDefault(s.charAt(i), 0) + 1);
        }
        
        for(int i = 0; i < s.length(); ++i){
            int cnt = count.get(s.charAt(i));
            if ( s.charAt(i) < s.charAt(pos)) pos = i;
            if (cnt == 1) {
                break;
            }
            count.put(s.charAt(i), --cnt);
        }
        return  "" + s.charAt(pos) + removeDuplicateLetters(s.substring(pos + 1).replaceAll("" + s.charAt(pos), ""));
    }
}