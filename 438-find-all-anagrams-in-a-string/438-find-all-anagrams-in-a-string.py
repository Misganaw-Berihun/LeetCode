class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []
        dict1 = [0 for i in range(26)]
        dict2 = [0 for i in range(26)]
        cnt = 0
        ans = []
               
        for i in range(m):
            dict1[ord(s[i]) - 97] += 1
            dict2[ord(p[i]) - 97] += 1
            
        for i in range(26):
            if dict1[i] == dict2[i]:
                cnt += 1
        
        for i in range(n - m):
            r, l = ord(s[i+m]) - 97, ord(s[i]) - 97
            
            if cnt == 26:
                ans.append(i)
            
            dict1[r] += 1
            if dict1[r] == dict2[r]:
                cnt += 1
            elif dict1[r] == dict2[r] + 1:
                cnt -= 1
                
            dict1[l] -= 1
            if dict1[l] == dict2[l]:
                cnt += 1
            elif dict1[l] == dict2[l] - 1:
                cnt -= 1
                
        if cnt == 26:
            ans.append(n - m)
            
        return ans