class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        visited = defaultdict(int)
        count = 0
        visited[0] = 1
        
        for val in nums:
            total += val
            count += visited.get(total - k,0)
            visited[total] += 1       
            
        return count
        