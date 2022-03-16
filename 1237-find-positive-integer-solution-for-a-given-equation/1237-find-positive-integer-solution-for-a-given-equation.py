"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def binarySearchY(self,customfunction,z):
        left = 0
        right = 1000
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if customfunction.f(1,mid) >= z:
                right = mid - 1
            else:
                left = mid + 1
                
        return left
            
    def binarySearchX(self,customfunction,z):
        left = 0
        right = 1000
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if customfunction.f(mid,1) >= z:
                right = mid - 1
            else:
                left = mid + 1
                
        return left
    
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        limit1 = self.binarySearchX(customfunction,z)
        limit2 = self.binarySearchY(customfunction,z)
        ans = []
        
        for i in range(1,limit1 + 1):
            for j in range(1,limit2 + 1):
                if customfunction.f(i,j) == z:
                    ans.append([i,j])
    
        return ans

        