class Solution:
    def add(self, a, b, MOD):
        res = a + b
        
        if res >= MOD:
            res -= MOD
            
        return res
    
    def numOfSubarrays(self, arr: List[int]) -> int:
        '''
            odd - odd = even
            even - odd = odd
            odd - even = odd
            even - even = even
        '''
        modulous = defaultdict(int)
        cur, count = 0, 0
        modulous[cur] = 1
        MOD = 1_000_000_007
        
        for num in arr:
            cur += num
            mod = cur % 2
            count = self.add(count, modulous[1 - mod], MOD)
            modulous[mod] += 1
        
        return count