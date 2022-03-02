class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub_ptr = 0
        str_ptr = 0
            
        while sub_ptr < len(s) and str_ptr < len(t):
            if t[str_ptr] == s[sub_ptr]:
                sub_ptr += 1
            
            str_ptr += 1
            
        return sub_ptr == len(s)
        