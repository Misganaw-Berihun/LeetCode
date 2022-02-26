class Solution:
    def compress(self, chars: List[str]) -> int:
        i , j = 0,1
        k = 0
        count = 1
        chars.append(" ")
        l = len(chars)
        
        while j < l:
            if chars[i] == chars[j]:
                count += 1
                
            if chars[i] != chars[j]:        
                if count != 1:
                    temp = chars[i] + str(count)
                
                    for ch in temp:
                        chars[k] = ch
                        k += 1
            
                else:
                    chars[k] = chars[i]
                    k += 1
                
                i = j
                count = 1
                
            j += 1   
        
        while k < l:
            chars.pop()
            k += 1
            
            
        
                
                
        