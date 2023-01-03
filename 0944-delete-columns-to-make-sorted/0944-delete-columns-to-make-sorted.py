class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        num_words = len(strs)
        len_of_each_word = len(strs[0])
        unsorted_columns = 0
        inbound = lambda x: x < num_words
        
        for i in range(len_of_each_word):
            correct_order = True
            j = 1
            
            while inbound(j) and correct_order:
                cur_char = strs[j][i]
                prev_char = strs[j - 1][i]
                
                if (cur_char < prev_char):
                    correct_order = False
                
                j += 1
            
            if not correct_order:
                unsorted_columns += 1
        
        return unsorted_columns
        