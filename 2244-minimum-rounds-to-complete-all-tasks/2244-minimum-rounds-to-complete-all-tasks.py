class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        '''
            2: 3, 3: 2 4: 5
            
            13 - (2 - 2) = 9
            
            % == 1 ... subtract 4
            % == 2 ... subract 2
            % == 0 ....subtract = 0
            
        '''
        num_tasks = len(tasks)
        count = Counter(tasks)
        min_operations = 0
        can_complete = True
        
        for key in count.keys():
            cur_count = count[key]
            if cur_count % 3 == 1:
                cur_count -= 4
                min_operations += 2
                
            elif cur_count % 3 == 2:
                cur_count -= 2
                min_operations += 1
               
            if (cur_count < 0):
                can_complete = False
                break
            
            min_operations += (cur_count // 3)
        
        answer = -1
        if can_complete:
            answer = min_operations
        
        return answer