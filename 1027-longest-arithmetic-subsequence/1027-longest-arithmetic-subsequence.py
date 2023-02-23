class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        '''
            an = a1 + (n-1) * d
            
        '''
        n = len(nums)
        ans = 0
        for i in range(-500, 501):
            sequence = defaultdict(int)
            last = -1
            for num in nums:
                sequence[num] = sequence[num-i] + 1
                last = max(last, sequence[num])
            
            ans = max(last, ans)
        
        return ans