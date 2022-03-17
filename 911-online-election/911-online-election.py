class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.d = defaultdict(int)
        self.d2 = defaultdict(int)
        cnt = 1
        j = 0
        mcnt = 1
        
        for i in range(len(self.persons)):
            cnt = self.d2[self.persons[i]] + 1
            if cnt >= mcnt:
                self.d[i] = i
                mcnt = cnt 
                j = i
            else:
                self.d[i] = j
                
            self.d2 [self.persons[i]] = cnt
            
    def binarySearch(self,t):
        l = 0
        r = len(self.times) - 1
        
        while l  <= r:
            m = l + (r - l ) // 2
            
            if self.times[m] > t:
                r = m - 1
            else:
                l = m + 1

        return r 
    
    def q(self, t: int) -> int:
        idx = self.binarySearch(t)
        return self.persons[self.d[idx]]
        
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)