class Solution:
    def numberOfSteps(self, num: int) -> int:
        binary = bin(num)
        return binary.count('1') + len(binary) - 3
            
        