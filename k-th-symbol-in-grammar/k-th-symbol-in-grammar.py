class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        else:
            t = (k + 1) // 2
            if k % 2 == 0:
                temp = self.kthGrammar(n-1,t)
                if temp == 0:
                    return 1
                else:
                    return 0
            else:
                return self.kthGrammar(n-1,t)
                
                
                
            
                
                
                
            

                
      
        