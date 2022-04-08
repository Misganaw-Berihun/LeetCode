class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #returns the days required to ship packages if max weight of ship is weight
        def helper(weight):
            n = len(weights)
            d = 1
            weight_sum = 0
            for i in range(n):
                weight_sum += weights[i]
                if weight_sum > weight:
                    weight_sum = weights[i]
                    d += 1
            return d 
        
        left, right = max(weights),  sum(weights) 
        while left < right:
            mid = left + (right - left) // 2
            d = helper(mid)
            
            if  d > days:
                left = mid + 1
            else:
                right = mid
        return left
        
            