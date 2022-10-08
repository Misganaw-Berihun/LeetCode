class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0 for i in range(1001)]
        
        for numPass, fro, to in trips:
            if numPass > capacity:
                return False
            prefix[fro] += numPass
            prefix[to] -= numPass
        
        for i in range(1,1001):
            prefix[i] += prefix[i-1]
            if prefix[i] > capacity:
                return False
        
        return prefix[1000] == 0
        