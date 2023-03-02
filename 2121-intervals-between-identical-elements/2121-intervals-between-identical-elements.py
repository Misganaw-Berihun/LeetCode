class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        length = len(arr)
        indices = defaultdict(list)
        prefix = [0 for i in range(length)]
        suffix = [0 for i in range(length)]
        ans = [0 for i in range(length)]
        
        for index, value in enumerate(arr):
            indices[value].append(index)
        
        for key, lst in indices.items():
            cnt = 1
            n = len(lst)
            
            for idx in range(1, n):
                temp = (lst[idx] - lst[idx - 1]) * cnt
                prefix[lst[idx]] = prefix[lst[idx - 1]]  + temp
                cnt += 1
            
            cnt = 1
            for idx in range(n - 2, -1, -1):
                temp = (lst[idx + 1] - lst[idx]) * cnt
                suffix[lst[idx]] =  suffix[lst[idx + 1]] + temp
                cnt += 1
        
        for i in range(length):
            ans[i] = (prefix[i] + suffix[i])
        
        return ans
        