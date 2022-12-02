class Solution:
    def build_graph(self, cur, adjList):
        if not cur:
            return 
        if cur.left:
            adjList[cur.val].append(cur.left.val)
            adjList[cur.left.val].append(cur.val)
        if cur.right:
            adjList[cur.val].append(cur.right.val)
            adjList[cur.right.val].append(cur.val)
        self.build_graph(cur.left, adjList)
        self.build_graph(cur.right, adjList)
        
    def bfs(self, adjList, start, k):
        ans = []
        queue = deque()
        queue.append((start, 0))
        visited = set()
        visited.add(start)
        
        cont = True
        while queue and cont:
            n = len(queue)
            for i in range(n):
                cur, level = queue.popleft()
                if level == k:
                    ans.append(cur)
                
                if level > k:
                    cont = False
                
                for nxt in adjList[cur]:
                    if nxt in visited:
                        continue
                    queue.append((nxt, level + 1))
                    visited.add(nxt)
        return ans
                
            
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adjList = defaultdict(list)
        self.build_graph(root, adjList)
        ans = self.bfs(adjList, target.val, k)
        return ans
