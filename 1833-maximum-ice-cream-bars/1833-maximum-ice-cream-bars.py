class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        size = len(costs)
        costs.sort()
        
        i = 0
        cur_cost = 0
        while i < size and  cur_cost + costs[i] <= coins:
            cur_cost += costs[i]
            i += 1
        
        return i
            
        