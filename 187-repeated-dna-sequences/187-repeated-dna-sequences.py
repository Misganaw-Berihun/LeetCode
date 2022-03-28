class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        occured = dict()
        ans = []
        
        for i in range(len(s) - 9):
            temp = s[i: i + 10]
            seen_before = occured.get(temp)
            if seen_before == None:
                occured[temp] = 1
            else:
                if occured[temp] != -1:
                    ans.append(temp)
                    occured[temp] = -1
                
        return ans
        