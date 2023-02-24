class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam = defaultdict(set)
        
        for id, t in logs:
            uam[id].add(t)
        
        count = defaultdict(int)
        for key in uam:
            count[len(uam[key])] += 1
        
        ans = []
        for i in range(1, k + 1):
            ans.append(count[i])
        
        return ans
        