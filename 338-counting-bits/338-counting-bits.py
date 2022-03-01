class Solution:
    def countBits(self, n: int) -> List[int]:
        acc = [0,1,1,2]
        
        if n <= 3:
            return acc[0:n+1]
        else:
            pow = 2
            
            for i in range(4,n+1):
                if i == 2*pow:
                    acc.append(1)
                    pow *= 2
                else:
                    dif = i - pow
                    acc.append( 1 + acc[dif])
                    
                    
        return acc
                    