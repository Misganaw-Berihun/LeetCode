class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        ans = [1]
        
        while len(ans) <= n:
            last = ans[-1]
            
            heappush(heap, 2 * last)
            heappush(heap, 3 * last)
            heappush(heap, 5 * last)
            
            top = heappop(heap)
            while top == ans[-1]:
                top = heappop(heap)
            ans.append(top)
        
        return ans[n-1]