class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)#frequency of each element
        ans = []
        
        changed.sort()
        
        for val in changed:
            freq = count[val] 
            
            if freq:#are there any unused values of val?
                count[val] -= 1 #is used hence subtract 1 from freq of val
                double = 2 * val
                double_idx = count.get(double)
                
                if double_idx: #val * 2 in changed?
                    ans.append(val)
                    count[double] -= 1 #doulbe is used hence subtract 1 from freq of double
                else: #val * 2 not in changed
                    return []
            else:  #if all values of val are used
                continue
                
        return ans
        
       
                
        
                
        
       
                
        
        
                
        
                
                
            
            
            
        
        
        
        
        
        
                
        
                
        
                
        
        
       
            
    
            
            
        