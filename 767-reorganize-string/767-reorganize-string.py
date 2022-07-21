class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        lst = []
        ans = []
        for k, v in count.items():
            heappush(lst,(-v, k)) 
        
        while lst:
            top1 = heappop(lst)
            ans.append(top1[1])
            if not lst and top1[0] != -1:
                return ""
            
            if not lst:
                break
            
            top2 = heappop(lst)
            ans.append(top2[1])
            t1 = top1[0] + 1
            t2 = top2[0] + 1
            if t1 != 0:
                heappush(lst, (t1, top1[1]))
            if t2 != 0:
                heappush(lst, (t2, top2[1]))
        
        return ''.join(ans)
            