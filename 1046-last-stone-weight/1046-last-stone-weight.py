class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda a: -a,stones))
        heapify(stones)
        
        while len(stones) > 1:
            first_heavy = heappop(stones)
            second_heavy = heappop(stones)
            
            if first_heavy != second_heavy:
                second_heavy = -1 * first_heavy - -1 * second_heavy
                heappush(stones,-1*second_heavy)
                
        if stones:
            return -1*stones[0]
        else:
            return 0
                
        