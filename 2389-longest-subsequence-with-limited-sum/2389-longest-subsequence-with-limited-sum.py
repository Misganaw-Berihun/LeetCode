class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        '''
            4 5 2 1
            3 10 21
            
            2 1
        '''
        size = len(nums)
        nums.sort()
        summ = sum(nums)
        ans = []
        
        for query in queries:
            ptr = size - 1
            num_elts = size
            cur = summ
            
            while cur > query:
                cur -= nums[ptr]
                ptr -= 1
                num_elts -= 1
            
            ans.append(num_elts)
        
        return ans
        