class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        NUM_ALP = 26
        OFFSET = ord('a')

        count = [0 for _ in range(NUM_ALP)]
        cur_count = [0 for _ in range(NUM_ALP)]
        
        for ch in s:
            index = ord(ch) - OFFSET
            count[index] += 1
        
        palindromes = set()
        for ch in s:
            index = ord(ch) - OFFSET
            for j in range(26):
                left_cnt = cur_count[j]
                right_cnt = count[j] - left_cnt
                
                if index == j:
                    right_cnt -= 1
                
                if left_cnt > 0 and right_cnt > 0:
                    palindrome = str(j) + ch
                    palindromes.add(palindrome)
            
            cur_count[index] += 1
        
        return len(palindromes)