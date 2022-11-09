class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        occurence = Counter(nums)
        dup = -1
        missing = -1
        
        for i in range(1,len(nums) + 1):
            if occurence[i] == 2:
                dup = i
            if i not in occurence.keys():
                missing = i
                
        return [dup,missing]
            
        