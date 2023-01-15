class Solution:
    def fill(self, v1, v2):
        for i in range(len(v2) - len(v1)):
            v1.append('0')
        return v1
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        
        length1 = len(ver1)
        length2 = len(ver2)
        length = max(length1, length2)
        i = 0
        ans = 0
        
        while ans == 0 and i < length:
            val1, val2 = 0, 0
            if i < length1:
                val1 = int(ver1[i])
            
            if i < length2:
                val2 = int(ver2[i])
            
            if val1 < val2:
                ans = -1
            
            elif val1 > val2:
                ans = 1
                
            i += 1
        
        return ans