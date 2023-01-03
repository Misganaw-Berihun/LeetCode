class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        size = len(nums)
        prev_smaller = [inf for i in range(size)]
        prev_greater = [inf for i in range(size)]
        dec_stk = []
        inc_stk = []
        
        for i in range(size):
            while dec_stk and nums[dec_stk[-1]] <= nums[i]:
                dec_stk.pop()
            
            while inc_stk and nums[inc_stk[-1]] >= nums[i]:
                inc_stk.pop()
                
            if dec_stk:
                prev_greater[i] = dec_stk[-1]
                
            if inc_stk:
                prev_smaller[i] = inc_stk[-1]
            
            dec_stk.append(i)
            inc_stk.append(i)
        
        pattern_exists = False
        index = 0
        while index < size and not pattern_exists:
            greater = prev_greater[index]
            smaller = inf
            if (greater != inf):
                smaller = prev_smaller[greater]
                while smaller != inf and (nums[smaller] >= nums[index]):
                    smaller = prev_smaller[smaller]

            pattern_exists = (smaller != inf and (nums[smaller] < nums[index]))
            index += 1
        
        return pattern_exists