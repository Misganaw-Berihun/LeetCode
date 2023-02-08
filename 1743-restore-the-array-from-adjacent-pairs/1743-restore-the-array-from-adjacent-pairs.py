class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neighbours = defaultdict(list)
        length = len(adjacentPairs) 
        
        for x, y in adjacentPairs:
            neighbours[x].append(y)
            neighbours[y].append(x)

        
        result = []
        for k in neighbours:
            if len(neighbours[k]) == 1:
                result.append(k)
                result.append(neighbours[k][0])
                break
        
        
        for i in range(len(neighbours) - 2):
            last = result[-1]
            prev = result[-2]
            
            cur = neighbours[last]
            if cur[0] != prev:
                result.append(cur[0])
            else:
                result.append(cur[1])
            
        
        return result        