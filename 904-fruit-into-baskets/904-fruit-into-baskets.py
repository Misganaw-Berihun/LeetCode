class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        occurence  = defaultdict(int)
        i = 0
        ret = 0
        length = 0
        
        for j in range(len(fruits)):
            occurence[fruits[j]] += 1
            
            if len(occurence) > 2:
                while i < len(fruits) and occurence[fruits[i]] != 1:
                    occurence[fruits[i]] -= 1
                    i += 1
                
                occurence.pop(fruits[i]) 
                length = j - i
                i += 1
            else:
                length += 1
                ret = max(ret,length)
        
        return ret
        
        
        
            
                
            
        