class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        count = defaultdict(int)
        
        for num in time:
            mod = num % 60
            temp = (60 - mod) % 60
            
            if temp in count:
                ans += count[temp]
        
            count[mod] += 1
        return ans
        