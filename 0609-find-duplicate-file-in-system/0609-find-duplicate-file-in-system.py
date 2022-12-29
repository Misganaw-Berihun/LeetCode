class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        size = len(paths)
        directories = defaultdict(list)
        
        for p in paths:
            tmp = p.split()
            for j in range(1, len(tmp)):
                d, c = tmp[j].split('(')
                content = c[:-1]
                t = tmp[0] + '/' + d
                directories[content].append(t)
        
        ans = []
        for key in directories:
            if len(directories[key]) > 1:
                ans.append(directories[key])
        
        return ans
            