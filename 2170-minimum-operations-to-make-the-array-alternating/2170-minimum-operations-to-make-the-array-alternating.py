class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def helper(d,key):
            p = 0
            ret = 0
            for (k,v) in d.items():
                if k != key and d[k] > p:
                    p = d[k]
                    ret = k
            return ret
        
        odd= defaultdict(int)
        even = defaultdict(int)
        
        n, m, j, e,o = len(nums), 0, 0, 0, 0
        for i in range(n):
            val = nums[i]
            if i % 2 == 0:
                even[val] += 1
                if even[val] > m:
                    m = even[val]
                    e = val
            else:
                odd[val] += 1
                if odd[val] > j:
                    j = odd[val]
                    o = val
                    
        l = -1
        if o == e:
            l = max(odd[o] + even[helper(even,e)],even[e] + odd[helper(odd,o)])
            
        return n -  even[e] - odd[o] if l == -1 else n  - l
                