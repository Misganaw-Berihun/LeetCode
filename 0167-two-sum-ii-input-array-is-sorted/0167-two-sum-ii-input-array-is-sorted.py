class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        left = 0
        right  = size - 1
        
        while left < right:
            summ = numbers[left] + numbers[right]
            
            if summ == target:
                return [left + 1, right + 1]
        
            elif summ < target:
                left += 1
                
            else:
                right -= 1
        
        