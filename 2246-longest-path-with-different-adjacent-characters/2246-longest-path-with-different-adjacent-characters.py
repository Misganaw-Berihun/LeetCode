class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        size = len(parent)
        adjList = defaultdict(list)
        
        for i in range(1, size):
            adjList[parent[i]].append(i)
        
        ans = 1
        def dfs(cur, prev):
            nonlocal size, ans
            if not adjList[cur]:
                if s[cur] != prev:
                    return 1
                return 0
            
            max1, max2 = 0, 0
            for next in adjList[cur]:
                val = dfs(next, s[cur])
                if val >= max1:
                    max2 = max1
                    max1 = val
                elif val > max2:
                    max2 = val
            
            ans = max(ans, max1 + max2 + 1)
            if s[cur] == prev:
                max1 = max2 = -1
            return max1 + 1
        dfs(0, "") 
        return ans