class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        left = 0
        countOf = defaultdict(int)
        distinct = 0
        
        for right in range(n):
            countOf[fruits[right]] += 1
            if countOf[fruits[right]] == 1:
                distinct += 1
            
            if distinct > 2:
                countOf[fruits[left]] -= 1
                if countOf[fruits[left]] == 0:
                    distinct -= 1
                
                left += 1
        
        return n - left
        