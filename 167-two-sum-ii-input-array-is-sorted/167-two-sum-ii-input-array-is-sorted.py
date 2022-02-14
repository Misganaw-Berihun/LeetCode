class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        occur = {}
        ans = []
        
        for i in range(len(numbers)):
            num = target - numbers[i]
            
            if occur.get(num):
                ans.append(occur[num])
                ans.append(i + 1)
                
                return ans
            else:
                occur[numbers[i]] = i + 1
                
                
                
            
        