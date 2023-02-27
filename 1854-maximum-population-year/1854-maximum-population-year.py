class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0 for _ in range(101)]
        for birth, death in logs:
            population[birth - 1950] += 1
            population[death - 1950] -= 1
        
        for i in range(1, 101):
            population[i] += population[i - 1]
        
        index = 0
        for i in range(1, 101):
            if population[i] > population[index]:
                index = i
        
        return (1950 + index)