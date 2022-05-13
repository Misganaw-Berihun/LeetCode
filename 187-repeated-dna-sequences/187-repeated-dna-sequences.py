class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        def bitMask(temp):
            mask = 0
            
            for i in range(10):
                if temp[i] == 'A':
                    mask |= 1 << i
                    
            for i in range(10, 20):
                if temp[i % 10] == 'C':
                    mask |= 1 <<i
            
            for i in range(20, 30):
                if temp[i % 10] == 'G':
                    mask |= 1 << i
            
            for i in range(30, 40):
                if temp[i % 10] == 'T':
                    mask |= 1 << i
                    
            return mask
        occured = dict()
        ans = []
        
        for i in range(len(s) - 9):
            temp = s[i: i + 10]
            mask = bitMask(temp)
            seen_before = occured.get(mask)
            if seen_before == None:
                occured[mask] = 1
            else:
                if occured[mask] != -1:
                    ans.append(temp)
                    occured[mask] = -1
                
        return ans
        