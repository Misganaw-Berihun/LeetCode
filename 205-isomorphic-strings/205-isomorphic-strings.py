class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n =len(s)
        dict_ = {}
        for i in range(n):
            if s[i] not in dict_:
                if t[i] in dict_.values():
                    return False
                dict_[s[i]] = t[i]
            else:
                if dict_[s[i]] != t[i] :
                    return False
        return True
                
            
                
                
            
 
                
             
            
        