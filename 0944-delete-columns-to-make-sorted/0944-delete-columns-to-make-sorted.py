class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        num_words = len(strs)
        len_of_each_word = len(strs[0])
        unsorted_columns = 0
        
        for i in range(len_of_each_word):
            correct_order = True
            j = 1
            
            while j < num_words and correct_order:
                if (strs[j][i] < strs[j - 1][i]):
                    correct_order = False
                
                j += 1
            
            if not correct_order:
                unsorted_columns += 1
        
        return unsorted_columns
        