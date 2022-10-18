class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        num_str = str(num)
        num_len = len(num_str)
        if num_len == 1:
            return num % 2 == 0
        start_num = 10 ** (num_len - 2)
        valid = False
        cur = start_num if num != 0 else 0
        
        while not valid  and cur <= num:
            cur_subtracted = num - cur
            cur_subtracted_str = str(cur_subtracted)
            cur_str = str(cur)
            leading_zeros = '0' * (len(cur_str) - len(cur_subtracted_str))
            cur_subtracted_reversed = cur_subtracted_str[::-1] + leading_zeros
            
            if cur_subtracted_reversed == cur_str:
                valid = True
            
            cur += 1
        
        return valid