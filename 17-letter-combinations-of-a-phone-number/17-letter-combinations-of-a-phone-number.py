class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def findComb(i, s):
            if i < 0:
                ans.append(''.join(s))
                return 
            for ch in references[digits[i]]:
                s[i] = ch
                findComb(i - 1, s)
        
        references = {
                            "2" : ["a", "b", "c"],
                            "3": ["d", "e", "f"],
                            "4": ["g", "h", "i"],
                            "5": ["j", "k", "l"],
                            "6": ["m","n","o"],
                            "7": ["p","q","r","s"],
                            "8": ["t", "u", "v"],
                            "9": ["w", "x", "y","z"]
                        }
        ans = []
        if digits == "":
            return []
        temp = [0 for i in range(len(digits))]
        findComb(len(digits) - 1, temp)
        return ans
        