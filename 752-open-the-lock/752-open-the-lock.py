class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        queue.append(list("0000"))
        visited = set(deadends)
        if ("0000" in visited):
            return -1
        ans = 0
        
        while queue:
            N = len(queue)
            
            for i in range(N):
                cur = queue.popleft()
                
                if ''.join(cur) == target:
                    return ans

                
                for j in range(len(cur)):
                    new_cur1 = cur.copy()
                    new_cur2 = cur.copy()
                    new_cur1[j] = str((int(cur[j]) + 1) % 10)
                    new_cur2[j] = str((int(cur[j]) - 1) % 10)
                    joined1 = ''.join(new_cur1)
                    joined2 = ''.join(new_cur2)
                    if joined1 not in visited:
                        queue.append(new_cur1)
                        visited.add(joined1)
                    if joined2 not in visited:
                        queue.append(new_cur2)
                        visited.add(joined2)
            ans += 1
        return -1
                        
                    
        
        