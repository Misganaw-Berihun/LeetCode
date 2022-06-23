class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n  = len(customers)
        curTime = customers[0][0]
        waitingTime = 0
        
        for arrival, time in customers:
            waitingTime += time
            if curTime >= arrival:
                waitingTime += curTime - arrival
            else:
                curTime += (arrival - curTime)
            curTime += time
        
        return waitingTime/ n