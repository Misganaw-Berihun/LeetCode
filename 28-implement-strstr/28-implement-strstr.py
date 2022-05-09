class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack)):
            j = 0
            k = i
            while k < len(haystack) and needle[j] == haystack[k]:
                j += 1
                k += 1
                if j == len(needle):
                    return i
                
        return -1
            
        