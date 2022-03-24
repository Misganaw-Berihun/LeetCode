class Solution:
    def arrangeCoins(self, n: int) -> int:
        complete_rows = 0
        cur_row = 1
        tot_coins  = 0
        
        while tot_coins <= n:
            complete_rows += 1
            tot_coins += cur_row
            cur_row += 1
            
        return complete_rows - 1
        