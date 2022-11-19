class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cur = 0
        steps = 0
        
        for i in range(len(plants)):
            if cur + plants[i] > capacity:
                steps += (2 * i)
                cur = 0
            cur += plants[i]
            steps += 1
        
        return steps
        