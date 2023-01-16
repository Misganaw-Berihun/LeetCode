class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
            [[1, 3], [6, 9]]
                  2, 5
                  
             [[1, 5], [6, 9]]
                  2 , 4
                  
            [[1, 6], [3, 9]]
                  4, 5
                  
        '''
        intervals.append(newInterval)
        length = len(intervals)        
        merged = []
        intervals.sort()
        
        start, end = intervals[0]
        for i in range(1, length):
            x, y = intervals[i]
            if x <= end:
                end = max(y, end)
            else:
                merged.append([start, end])
                start = x
                end = y
        
        merged.append([start, end])
        return merged