class Solution {
    private static long numStrings(int len, char cur, char [] vowels,
                                  Map<Character, Set<Character>> order,
                                  Map<Character, Integer> charToIdx,
                                  long [][] memo){
            if (len == 0) return 1;
            int idx = charToIdx.get(cur);
            if (memo[len][idx] != 0) return memo[len][idx];
            long num = 0;
            for (char v: vowels){
                if (order.get(cur).contains(v)){
                    num += numStrings(len - 1, v, vowels, order, charToIdx, memo);
                }
            }
            memo[len][idx] = num % 1000000007;
            return memo[len][idx];
    }
    
    public int countVowelPermutation(int n) {
        HashMap<Character, Set<Character>> order = 
                    new HashMap<Character, Set<Character>> ();
        char [] vowels = {'a', 'e', 'i', 'o', 'u'};
        long [][] memo = new long[n + 1][5];
        Map<Character, Integer> charToIdx = 
                            new HashMap<Character, Integer>();
        
        charToIdx.put('a', 0);
        charToIdx.put('e', 1);
        charToIdx.put('i', 2);
        charToIdx.put('o', 3);
        charToIdx.put('u', 4);
        
        
        order.put('a', new HashSet<Character>(Arrays.asList('e')));
        order.put('e', new HashSet<Character>(Arrays.asList('a', 'i')));
        order.put('i', new HashSet<Character>(Arrays.asList('a', 'e', 'o', 'u')));
        order.put('o', new HashSet<Character>(Arrays.asList('i', 'u')));
        order.put('u', new HashSet<Character>(Arrays.asList('a')));
        
        long ans = 0;
        for (char v: vowels){
            ans += numStrings(n - 1, v, vowels, order, charToIdx, memo);
        }
        return (int) (ans % 1000000007);
    }
}