class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        all_values = list(freq.values())
        max_value = max(all_values)
        
        num_max = all_values.count(max_value)
        empty_slots = (max_value - 1) * (n - num_max + 1)
        rest_tasks = len(tasks) - num_max * max_value
        num_idles = 0
        
        if empty_slots >= rest_tasks:
            num_idles = empty_slots - rest_tasks
        else:
            return len(tasks)
        
        return len(tasks) + num_idles
        
        
        
        
        