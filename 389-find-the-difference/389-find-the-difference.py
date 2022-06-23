class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict = defaultdict(int)
        for ch in s:
            pos = ord(ch) - ord('z') + 25
            num = 1 << pos
            dict[num] += 1
        
        for ch in t:
            pos = ord(ch) - ord('z') + 25
            temp = 1 << pos
            if (temp not in dict or dict[temp] == 0):
                return ch
            dict[temp] -= 1
            
                
            

        
        
        
        