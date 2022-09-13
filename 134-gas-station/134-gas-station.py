class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = -1
        cur = 0
        for i in range(n):
            rem = gas[i] - cost[i]
            cur += rem
            if rem >= cur:
                start = i
                cur = rem
        
        if start == -1:
            return start
        
        cnt = 0
        j = start
        cur = gas[start]
        while cnt < n:
            cur -= cost[j]
            if cur < 0:
                return -1
            j = (j + 1) % n
            cnt += 1
            cur += gas[j]
        return start
            
                