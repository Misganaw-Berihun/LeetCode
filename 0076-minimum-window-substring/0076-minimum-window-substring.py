class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        
        if n < m:
            return ""
        
        t_count = defaultdict(int)
        s_count = defaultdict(int)
        matched = 0
        
        for char in t:
            t_count[char] += 1
        
        left = 0
        min_window = inf
        start = -1
        for i in range(n):
            char = s[i]
            s_count[char] += 1
            if s_count[char] <= t_count[char]:
                matched += 1
                
            while matched >= m:
                char = s[left]
                s_count[char] -= 1
                if s_count[char] < t_count[char]:
                    matched -= 1
                left += 1
            
            cur_window = i - left + 2
            if left > 0 and min_window > cur_window:     
                min_window = min(cur_window, min_window)
                start = left - 1
        
        if start == -1:
            return ""
        return s[start: start + min_window]
            