class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        N1, N2 = len(nums1), len(nums2)
        heap = [(nums1[0] + nums2[0], 0, 0)]
        visited = set()
        ans = []
        visited.add((0, 0))
        while len(ans) < k and heap:
            s, a, b = heappop(heap)
            ans.append([nums1[a], nums2[b]])
            
            if b < N2 - 1 and a < N1 and (a, b+1) not in visited:
                s1 = nums1[a] + nums2[b + 1]
                heappush(heap, (s1, a, b+1))
                visited.add((a, b+1))
            
            if a < N1 - 1 and b < N2 and (a+1, b) not in visited:
                s2 = nums1[a+1] + nums2[b] 
                heappush(heap, (s2, a+1, b))
                visited.add((a+1, b))
            
        
        return ans