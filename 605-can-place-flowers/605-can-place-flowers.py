class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        for i in range( m ):
            if i == 0:
                if m>1 and flowerbed[i] == flowerbed[i+1]==0:
                    n -= 1
                    flowerbed[i] = 1
                elif m == 1 and flowerbed[i]==0:
                    n -= 1
            elif i == m-1:
                    if m>1 and flowerbed[i] == flowerbed[i-1]==0:
                        n -= 1
                        flowerbed[i] = 1                
        
            elif flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
                
        return n < 1
        