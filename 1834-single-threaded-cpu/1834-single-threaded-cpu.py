class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        heap = []
        new = []
        for index, (start, duration) in enumerate(tasks):
            new.append((start, duration, index))
            
        new.sort()
        index = 0
        time = new[0][0]
        answer = []
        
        while heap or index < n:
            while not heap or (index < n and time >= new[index][0]):
                start, duration, i = new[index]
                heappush(heap, (duration, i))
                index += 1
            
            if heap:
                duration ,i = heappop(heap)
                answer.append(i)
                time = max(start, time) + duration
        
        return answer