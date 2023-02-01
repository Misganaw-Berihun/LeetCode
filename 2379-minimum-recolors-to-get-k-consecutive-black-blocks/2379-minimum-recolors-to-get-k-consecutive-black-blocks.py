class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        number_of_blocks = len(blocks)
        black_count = 0
        
        for i in range(k):
            if blocks[i] == 'B':
                black_count += 1
        
        minimum_operations = (k - black_count)
        for i in range(k, number_of_blocks):
            if blocks[i] == 'B':
                black_count += 1
            
            if blocks[i - k] == 'B':
                black_count -= 1
                
            minimum_operations = min(minimum_operations, k - black_count)
        
        return minimum_operations