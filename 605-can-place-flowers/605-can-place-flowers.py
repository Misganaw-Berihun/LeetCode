class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        m = len(flowerbed)
        
        for i in range(1,m-1):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
                
        return n < 1
        