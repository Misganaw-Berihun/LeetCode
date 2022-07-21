class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        lst = []
        ans = ""
        for k, v in count.items():
            heappush(lst, (-v, k))
        
        while lst:
            top = heappop(lst)
            for i in range(-top[0]):
                ans += top[1]
        
        return ans
        
        
        