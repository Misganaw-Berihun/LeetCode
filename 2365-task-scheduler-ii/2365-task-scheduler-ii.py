class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_day = defaultdict(int)
        cur_day = 0
        
        for i in range(len(tasks)):
            cur_day += 1
            task = tasks[i]
            if task in last_day and (cur_day - last_day[task]) <= space:
                cur_day = last_day[task] + space + 1
            last_day[task] = cur_day
            
        return cur_day