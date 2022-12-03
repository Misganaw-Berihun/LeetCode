class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        heap = []
        size = len(s)
        
        for key, val in count.items():
            heappush(heap, (-val, key))
        
        ans = []
        while heap:
            freq, char = heappop(heap)
            ans.extend([char] * (-freq))
        
        return ''.join(ans)