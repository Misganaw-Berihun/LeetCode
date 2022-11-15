class Solution {
    public int romanToInt(String s) {
    HashMap<Character,Integer> map = new HashMap<>(){{
            put('I',1);
            put('V',5);
            put('X',10);
            put('L',50);
            put('C',100);
            put('D',500);
            put('M',1000);
        }};
        
        
        int number = 0;
        for(int i = 0; i < s.length(); i++){
            if(i != s.length() - 1 && map.get(s.charAt(i)) < map.get(s.charAt(i + 1)) ){
                number -= map.get(s.charAt(i));
            }else{
                number += map.get(s.charAt(i));
            }
        }
        
        return number;
    }
}