class Solution:
    def count(self, cur, adjlist, ans, labels, parent):
        ret = [0 for _ in range(26)]
        idx = ord(labels[cur]) - ord('a')
        ret[idx] = 1
        
        for nxt in adjlist[cur]:
            if nxt != parent:
                tmp = self.count(nxt, adjlist, ans, labels, cur)
                
                for i in range(len(tmp)):
                    ret[i] += tmp[i]
                               
        ans[cur] = ret[idx]
        return ret
        
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjlist = defaultdict(list)
        ans = [0 for _ in range(n)]
        
        for src, dst in edges:
            adjlist[src].append(dst)
            adjlist[dst].append(src)
        
        self.count(0, adjlist, ans, labels, -1)
        return ans
        