class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        size = len(nums)
        forward_prefix = [0 for i in range(size)]
        backward_prefix = [0 for i in range(size)]
        
        for i in range(firstLen):
            forward_prefix[firstLen - 1] += nums[i]
            
        for i in range(firstLen, size):
            forward_prefix[i] = forward_prefix[i-1] + nums[i] - nums[i - firstLen]
        
        for i in range(1, size):
            forward_prefix[i] = max(forward_prefix[i-1], forward_prefix[i])
        
        for i in range(-1, -firstLen-1, -1):
            backward_prefix[-firstLen] += nums[i]
            
        for i in range(-firstLen - 1, -size - 1, -1):
            backward_prefix[i] = backward_prefix[i+1] + (nums[i] - nums[i + firstLen])
        
        for i in range(size - 2, -1, -1):
            backward_prefix[i] = max(backward_prefix[i+1], backward_prefix[i])
        
        cur = 0
        for i in range(secondLen):
            cur += nums[i]
        
        ans = cur + backward_prefix[secondLen]
        for i in range(secondLen, size - 1):
            cur += (nums[i] - nums[i - secondLen])
            case1 = forward_prefix[i - secondLen] + cur
            case2 = backward_prefix[i + 1] + cur
            ans = max(ans, case1, case2)
           
        cur += (nums[size - 1] - nums[size - 1 - secondLen])
        ans = max(ans, cur + forward_prefix[size - secondLen - 1])
        return ans