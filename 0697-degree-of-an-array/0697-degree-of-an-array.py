class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        last_index = defaultdict(int)
        first_index = defaultdict(int)
        freq = defaultdict(int)
        cnt = 0
        
        for i, num in enumerate(nums):
            last_index[num] = i
            if num not in first_index:
                first_index[num] = i
            
            freq[num] += 1
            cnt = max(freq[num], cnt)
            
        smallest_length = n + 1
        for num in nums:
            cur_length = (last_index[num] - first_index[num] + 1)
            if freq[num] == cnt:
                smallest_length = min(cur_length, smallest_length)
        
        return smallest_length