class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        visited = set(deadends)
        begin = set()
        end = set()
        numSteps = 0
        begin.add("0000")
        end.add(target)
        
        while begin and end:
            temp = set()
            N = len(begin)
            for j in range(N):
                for move in list(begin):
                    if move in end:
                        return numSteps
                    if move in visited:
                        continue
                    visited.add(move)
                    for i in range(4):
                        curCharInc = move[:i] + str((int(move[i]) + 1)  % 10) + move[i+1:]
                        curCharDec = move[:i] + str((int(move[i]) - 1) % 10) + move[i+1:]
                        if curCharInc not in visited:
                            temp.add(curCharInc)
                        if curCharDec not in visited:
                            temp.add(curCharDec)
            numSteps += 1                
            begin = end.copy()
            end =  temp.copy()
        
        return -1