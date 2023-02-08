class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neighbours = defaultdict(list)
        length = len(adjacentPairs) 
        start = -1
        for x, y in adjacentPairs:
            neighbours[x].append(y)
            neighbours[y].append(x)

        
        for k in neighbours:
            if len(neighbours[k]) == 1:
                start = k
                break
        
        result = []
        result.append(start)
        visited =set()
        visited.add(start)
        
        for i in range(length):
            cur = result[-1]
            
            for nxt in neighbours[cur]:
                if nxt not in visited:
                    result.append(nxt)
                    visited.add(nxt)
        
        return result        